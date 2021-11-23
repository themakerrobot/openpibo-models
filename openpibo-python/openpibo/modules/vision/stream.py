# import the necessary packages
from threading import Thread
import cv2
import time

class VideoStream:
  def __init__(self, src=0, width=640, height=480, name="video_thread"):
    self.stream = cv2.VideoCapture(src)
    self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    (self.grabbed, self.frame) = self.stream.read()
    (self.grabbed, self.frame) = self.stream.read()
    (self.grabbed, self.frame) = self.stream.read()
    (self.grabbed, self.frame) = self.stream.read()
    (self.grabbed, self.frame) = self.stream.read()
    self.stopped = False 

  def start(self):
    t = Thread(target=self.update, name="video_thread", args=())
    t.daemon = True
    t.start()
    return self

  def update(self):
    while True:
      if self.stopped:
        self.stream.release()
        return
      (self.grabbed, self.frame) = self.stream.read()

  def read(self):
    return self.frame
     #return cv2.flip(self.frame, -1)

  def stop(self):
    self.stopped = True
    time.sleep(0.5)
