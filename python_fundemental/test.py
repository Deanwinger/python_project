import time, os

def run():
    n=0
    print('Run child process %s ...' % (os.getpid()))
    while n <5:
        n += 1
        print("countdown: " + str(n))
        time.sleep(1)


if __name__ == "__main__":
    run()


{'address': self.address,
 'age': self.age,
 'annual_income': self.annual_income,
 'car_property': self.car_property,
 'career': self.career,
 'company': self.company,
 'company_size': self.company_size,
 'credit': self.credit,
 'current_inve': self.current_inve,
 'duration': self.duration,
 'educational_background': self.educational_background,
 'end_time': self.end_time,
 'expected_rate': self.expected_rate,
 'fee': self.fee,
 'gender': self.gender,
 'house_property': self.house_property,
 'id_num': self.id_num,
 'industry': self.industry,
 'is_valid': self.is_valid,
 'matrimony': self.matrimony,
 'name': self.name,
 'participators': self.participators,
 'position': self.position,
 'purpose': self.purpose,
 'raise_money': self.raise_money,
 'repayment': self.repayment,
 'stage': self.stage,
 'start_time': self.start_time,
 'time_create': self.time_create,
 'title': self.title,
 'uid': self.uid,
 'work_seniority': self.work_seniority,}
