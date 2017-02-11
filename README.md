# AggressiveDoor
Initial Commit

This is supposed to be a space MUD. We'll see how that goes.

Whilst the old tcp echo client and server remain a new one using asyncio co-routines has been copy pasted in. 
Things to do:
0) Remove old client/server code
1) Get the server as a runnable object
2) Get the server printing out all the commands it received
3) Apply some sort of validation to the commands (say.... do_THE_THING should work but THE_THING shouldn't)
4) Implement requests in the server
5) Modify the client code so that you can send commands over a command line interface
6) Make the commands do something
7) ???
8) profit!
