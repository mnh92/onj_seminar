import Tester

folder = 'pan16-author-profiling-twitter-downloader/pan16-author-profiling-training-dataset-english-2016-04-25'
#folder = 'small_sample'
tester = Tester.Tester(folder)

k = 3
acc = 0.0
for _ in range(k):
    acc += tester.run_evaluation()

acc /= k

print('average accuracy: ', acc)
