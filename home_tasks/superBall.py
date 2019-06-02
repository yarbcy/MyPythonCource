# Create a class Ball.
# Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
  def __init__(self, arg=None):
      if arg == None:
          self.ball_type = "regular"
      elif arg == "super":
          self.ball_type = "super"
      else:
          self.ball_type = "regular"