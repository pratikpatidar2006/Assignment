"""

7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you


Output:


hello how are you
"""
n=input("Enter String :")
n1=n.split(" ")
visited=""
for ch in n1:
      if ch not in visited:
              visited=visited+" "+ch
      

print(visited)
        
         
          
   