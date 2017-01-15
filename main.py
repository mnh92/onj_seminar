import Tester

# path to folder with data
folder = 'pan16-author-profiling-twitter-downloader/pan16-author-profiling-training-dataset-english-2016-04-25'
tester = Tester.Tester(folder)
tester.run_evaluation()
