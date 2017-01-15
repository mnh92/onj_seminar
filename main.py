import Tester

folder = 'pan16-author-profiling-twitter-downloader/pan16-author-profiling-training-dataset-english-2016-04-25'
#folder = 'small_sample'
tester = Tester.Tester(folder)
tester.run_evaluation()
