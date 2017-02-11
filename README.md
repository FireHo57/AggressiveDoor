# AggressiveDoor
Initial Commit

This is supposed to be a space MUD. We'll see how that goes.

No more old style TCP Server. I've copied the example coroutine using server from the reference material into the Server folder and am working on that as the main stubb. I've implemented a dumping mechanism which just prints out all the commands that were run since the last time dump was called (and then deletes the log); currently this spits out to everyone which is somethign i'd like to change. maybe implement some way of knowing who the message came from and then only dumping to them (this would be nice in general in fact). Hey ho!

Things done:

(0)Remove old client/server code - DONE - wysiwyg
(1) Get the server as a runnable object - DONE - using new style server has enabled this
(2) Get the server printing out all the commands it received - DONE - see above
(6) Modify the client code so that you can send commands over a command line interface - OBSELETE -no changes in client neccesary, 
    new server allows this

Things to do:

(3) Implement one to one, one to many and one to all (but not self) messaging in server
(4) Apply some sort of validation to the commands (say.... do_THE_THING should work but THE_THING shouldn't)
(5) Implement requests in the server
(7) Make the commands do something
(8) ???
(9) profit!
