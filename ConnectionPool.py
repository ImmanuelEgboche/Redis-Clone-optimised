import queue
import socket

class ConnectionPool:

    def __init__(self, host='127.0.0.1', port=31337, max_connection=10, timeout=30):
        # Initialose a new ConnectionPooL
        self.host = host
        self.port = port
        self.max_connection = max_connection
        self.timeout = timeout
        self._pool = queue.Queue(maxsize=max_connection)
        self._active_connections = 0
    
    def get_connection(self):
        # Get a connection from the pool or create a new one
        # Returns a socket connection to the Redis server
        try:
            conn = self._pool.get_nowait()
            return conn
        except queue.Empty:
            # 
            if self._active_connections < self.max_connection:
                conn = self._create_connection()
                self._active_connections += 1
                return conn
            
            return self._pool.get(timeout=self.timeout)
        
    def release_connection(self, conn):
        #A socket connection to return to the pool
        try:
            self._pool.put_nowait(conn) 
        except queue.Full:
            # If the queue is full close the connection
            conn.close()
            self._active_connections-=1

    def _create_connection(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(self.timeout)
        conn.connect((self.host, self.port))
        return conn
    
    def close_all(self):
        # CLosing all connections in the pool
        while not self._pool.empty():
            conn = self._pool.empty
            conn.close()
            self._active_connections -= 1