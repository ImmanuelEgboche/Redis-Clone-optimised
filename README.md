- Buffer pooling reusing bytesIO to reduce memory allocation
- modified the procolhandler to use the buffer pool for all reponses
- adde resoure management to ensure budders are returned to the pool


- implementing connection ool calls that manages the pool of reusable socket 
- chamges to client class to use said connections and release after use 
- adding connection error handling and recovery mechs 
- imporved respirce managment

- created a optimised protocol handler with pre-coded common responses
- improved errror handling to avoid unnnescessary lookups 
- optimised string handling to reduce encoding/decoding operations