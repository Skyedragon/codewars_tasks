Task
There are several units in a line, out of your sight. You will be given a list of hints (a list or array of strings) that indicates who is next to who in the queue, and you have to rebuild the queue of people, in appropriate order.

Example
With these hints,

<code>
  "white has black on his left",
 "red has green on his right",
  "black has green on his left" </code>
you should reduce that the queue is the following:

<code> "red", "green", "black", "white" </code>
Notes:
It is always possible to reduce the complete order in the queue.
The hints can be of two different forms, such as "white has black on his left", or "black has white on his right".
Each queue has at least two units.
