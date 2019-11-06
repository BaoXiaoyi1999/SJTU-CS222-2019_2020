import random


# some improvement may be done concerning finding the list of last compatible job
#  maybe -> one pass instead of binary search?

random.seed(0)


def generate_job(job_num, duration, max_value):
    # each job: end_time, start_time, value
    job_list = []
    for i in range(job_num):
        temp_duration = random.randint(0, duration/2)
        temp_value = random.randint(1, max_value+1)
        temp_start = random.randint(0, duration - temp_duration)
        job_list.append((temp_start+temp_duration, temp_start, temp_value))
    return job_list


def distinct_end_time(job_list):
    if not job_list:
        return []
    start_end_value_list = [(item[1], item[0], item[2]) for item in job_list]
    start_end_value_list.sort()
    distinct_list = [start_end_value_list[0]]
    for i in range(1, len(start_end_value_list)):
        if start_end_value_list[i][0] == start_end_value_list[i-1][0]:  # start time is the same as the previous one
            pass
        else:
            distinct_list.append(start_end_value_list[i])
    end_start_value_list = [(item[1], item[0], item[2]) for item in distinct_list]
    return end_start_value_list


class WeightedIntervalScheduling:
    def __init__(self, jobs):
        self.job_list = jobs
        self.job_list.sort()  # sort job by their end time
        self.opt = self.opt_first_i_jobs()
        self.is_chosen = self.recover_chosen_jobs()

    def last_compatible(self, temp_job_index):
        start_time = self.job_list[temp_job_index][1]
        if not self.job_list:
            return -1
        if self.job_list[0][0] > start_time or temp_job_index == 0:
            return -1
        l = 0  # the first incompatible
        r = temp_job_index
        while l < r:
            mid = (l + r)//2
            if self.job_list[mid][0] < start_time:  # not big enough
                l = mid + 1
            elif self.job_list[mid][0] > start_time:  # not compatible
                r = mid
            else:  # exactly
                return mid  # the next
        return l - 1

    def opt_first_i_jobs(self):
        opt = [0]  # the best solution for the first i jobs(the jobs are sorted by end time)
        for i in range(len(self.job_list)):
            temp1 = opt[-1]  # if don't choose.
            value = all_jobs[i][2]
            ori = self.last_compatible(i)  # index of the last compatible job
            if ori != -1:
                temp2 = opt[ori+1] + value  # if choose the job. pay attention to index
            else:
                temp2 = value
            opt.append(max(temp1, temp2))
        return opt

    def recover_chosen_jobs(self):
        is_chosen = []
        for i in range(len(self.opt)-1):
            if self.opt[i] == self.opt[i+1]:
                is_chosen.append(0)  # the job is not chosen
            else:
                is_chosen.append(1)
        return is_chosen

    def display(self):
        print("All jobs:", self.job_list)
        print("Chosen jobs:")
        for index in range(len(self.job_list)):
            if self.is_chosen[index]:
                print("Job {0}, end_time = {1}, start_time = {2}, value = {3}".
                      format(index, self.job_list[index][0], self.job_list[index][1], self.job_list[index][2]) )
        print("Optimal solution:")
        print(self.opt)
        print("Total value = {0}".format(self.opt[-1]) )


job_num = 10
dur = 20
maxv = 10
all_jobs = generate_job(job_num, dur, maxv)
distinct_jobs = distinct_end_time(all_jobs)

solution = WeightedIntervalScheduling(distinct_jobs)
print(distinct_jobs)
for i in range(len(distinct_jobs)):
    print(solution.last_compatible(i))
solution.display()

