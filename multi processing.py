from multiprocessing import process,cpu_count
import time
def counter(num):
    count = 0
    while count < num:
        count+=1
def main():
  a = process(target=counter, args=(36,))
  a.start()
  a.join()

  print("finished in",time.perf_counter(),"second")

if __name__ == "__main__":
    main()