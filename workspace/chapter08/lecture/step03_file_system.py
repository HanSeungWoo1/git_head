import os # os 모듈 import

#현재 작업 디렉토리 경로 확인
print(os.getcwd())

#작업 디렉터리 변경 : `chapter08' 이동
os.chdir('chapter08')
os.getcwd() # 'D:\\Pywork\\workspace\\chapter08'

#현재 작업 디렉터리 목록 : list 반환
os.listdir('.') # ['.project', '.pydevproject', data', 'example', 'lecture']

#디렉터리 생성 : 'test'생성
os.mkdir('test')
os.listdir('.') # ['.project', '.pydevproject', data', 'example', 'lecture','test']

#디렉터리 이동 : 'test' 이동
os.chdir('test')
os.getcwd() # 'D:\\Pywork\\workspace\\chapter08\\test'

#여러 디렉터리 생성 : 'test2', 'test3' 생성
os.makedirs('test2/test3')
os.listdir('.') #['test2']

# 디렉터리 이동
os.chdir('test2')
os.listdir('.') # ['test3']

# 디렉터리 삭제 : 'test3' 삭제
os.rmdir('test3')
os.listdir('.') # []

# 상위 디렉터리 이동 : 상위 디렉터리 2개 이동
os.chdir('../..')
os.getcwd() # 'D:\\Pywork\\workspace\\chapter08'

# 여러 개의 디렉터리 삭제 : 'test', 'test2' 삭제
os.removedirs('test/test2')



import os.path

print(os.getcwd())

os.chdir('chapter08')
os.getcwd()

os.path.abspath('lecture/step01_try_except.py')

os.path.dirname('lecture/step01_try_except.py')

os.path.exists('D:\\git_office\\workspace')

os.path.isdir('lecture')

os.path.split('d:\\test\\test1.txt')

os.path.join('d:\\test','test1.txt')

os.path.getsize('lecture/step01_try_except.py')