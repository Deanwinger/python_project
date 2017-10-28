import re

class TempliteSyntaxError(ValueError):
    """Raised when a template has a syntax error."""
    pass

class CodeBuilder(object):
    """Build source code conveniently"""
    def __init__(self, ident=0):
        self.code = []
        self.indent_level = indent

    def __str__(self):
        return "".join(str(c) for c in self.code)

    def add_line(self, line):
        self.code.extend([" " * self.indent_level, line , "\n"])

    def add_section(self):
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    INDENT_STEP = 4

    def indent(self):
        self.indent_level +=  INDENT_STEP

    def dedent(self):
        self.indent_level -=  INDENT_STEP

    def get_globals(self):
        assert self.indent_level == 0
        python_source = str(self)
        global_namespace = {}
        exec(python_source, global_namespace)
        return global_namespace

class Templite(object):
    def __init__(self, text, *contexts):
        self.context = {}
        for context in contexts:
            self.context.update(context)

        self.all_vars = set()
        self.loop_vars = set()

        code = CodeBuilder()

        code.add_line("def render_function(context, do_dots):")
        code.indent()
        vars_code = code.add_section()
        code.add_line("result = []")
        code.add_line("append_result = result.append")
        code.add_line("extend_result = result.extend")
        code.add_line("to_str = str")

        buffered = []
        def flush_output():
            if len(buffered) == 1:
                code.add_line("append_result(%s)" %buffered[0])
            elif len(buffered) > 1:
                code.add_line("extend_result(%s)" % ", ".join(buffered))
            del buffered[:]

        ops_stack = []

        tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.？#})"， text)

        for token in tokens:
            if token startswith('{#'):
                continue
        elif token.startswith('{{'):
            expr = self._expr_code(token[2: -2].strip())
            buffered.append("to_str(%s)" % expr)
        elif token.startswith('{%'):
            flush_output()
            words = token[2:-2].strip().split()
            if words[0] == 'if':
                if len(words) != 2:
                    self._syntax_error("Don't understand if", token)
                ops_stack.append('if')
                code.add_line("if %s:" % self._expr_code(words[1]))
                code.indent()
            elif words[1] == 'for':
                if len(words) != 4 or words[2] != 'in':
                    self._syntax_error("Don't understand for", token)
                ops_stack.append('for')
                self._variable(words[1], self.loop_vars)
