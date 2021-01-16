# MIT License Copyright (c) 2021 Shinji Iida
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import sys
class Evaluator():

    def __init__(self, input_file):
        self.input_file        = input_file
        self.incompleted_tasks = []
        self.completed_tasks   = []
        self.n_done, self.n_tasks = 0, 0

    def eval(self):
        with open(self.input_file, 'r') as fin:
            for line in fin:
                line = line.strip() #remove the left and right spaces
                
                if line      == '': continue
                if line[0]   == '#': continue # skip commented out rows
                if line[0]   == '*': 
                    due_date = line.split(':')[-1]
                    print(f"\nDUE DATE: {due_date}")
                    continue

                if line[0:2] == '[]': 
                    self.incompleted_tasks.append(line[2:])
                elif line[1].lower() == 'x':
                    self.n_done += 1
                    self.completed_tasks.append(line[3:])
                else:
                    exit(f'Wrong syntax. Check below:\n {line}')   
                self.n_tasks += 1
        return self

    def showTasks(self, task_type):
        if task_type.lower()   == 'completed': 
            tasks = self.completed_tasks
        elif task_type.lower() == 'incompleted': 
            tasks = self.incompleted_tasks
        else:
            exit(f'Wrong type name: {task_type}')
            
        print(f'\n{task_type} tasks:')
        for i, task in enumerate(tasks): 
            print(f'    {i}. {task}')
            if i == 2: 
                print('    etc.')
                break

        return self

    def showProgress(self):
        progress_ratio = 100.0*(self.n_done/self.n_tasks)
        print(f'\nProgress: {self.n_done}/{self.n_tasks} = {progress_ratio:.2f}% has been done!')
        bar = '|' + ''.join('#' for i in range(self.n_done))
        bar = bar + ''.join('-' for i in range(self.n_tasks - self.n_done)) + '|'
        print(f'Progress Bar: {bar}\n')
        if progress_ratio == 100.0:
            exit("YOU'VE COMPLETED! WELL DONE!!")
        elif progress_ratio >= 50.0:
            print("YOU'VE REACHED THE HALF! STAY MOTIVATED!") 
        return self

def main():
    EV = Evaluator(sys.argv[1])
    EV.eval()
    EV.showProgress()
    EV.showTasks(task_type='incompleted')
    EV.showTasks(task_type='completed')
   
if __name__ == '__main__':
    main()