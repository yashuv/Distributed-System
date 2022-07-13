# Distributed-System

I tried to give some insights and provide the simulated code for the Election Algorithm (Bully and Ring), RPC and RMI, and Clock Synchronization using Lamport logical timestamp and Vector timestamp.
<br><br>
------------------------------------- <b>  Clock Synchronization In Distributed System </b>---------------------------------------------------------- <br>
  🔶<b> Using Lamport’s Algorithm </b><br><br>
  ![image](https://user-images.githubusercontent.com/66567559/178660323-a7f54e82-a30e-41ff-9d28-08e89d60dfe6.png)
<br><br>
  Program Output:<br>
  ![image](https://user-images.githubusercontent.com/66567559/178660732-bf7b4900-9ebc-4ba1-8a7c-9633c555d7a7.png)
<br><br>
  🔶<b> Using Vector Timestamp </b> <br><br>
 ![image](https://user-images.githubusercontent.com/66567559/178661244-3e5166f1-b3c6-455a-974c-790795c12c8e.png)
<br><br>
 Program Output:<br>
 ![image](https://user-images.githubusercontent.com/66567559/178661419-06cec436-2567-42cd-a546-4397011f03d9.png)
<br>

---------------------------------------- <b> Leader Election in Distributed System </b>---------------------------------------------------------- <br>
The main purpose of the leader election is to choose a node as a coordinator. It will act as a leader and coordinate activities of the whole system.The election algorithm assumes that every active process in the system has a unique priority number. A leader in any leader election algorithm is usually chosen based on the node which has the largest identifier. Hence, when a coordinator fails, this algorithm elects the active process that has the highest priority number. Then this number is sent to every active process in the distributed system.<br><br>
  🔶<b> Bully Algorithm </b><br><br>
  In a distributed system, when the leader is crashed, other nodes must elect another leader. The election algorithm we consider here is called the bully algorithm because the node with the highest ID forces the nodes with smaller ID into accepting it as a coordinator.<br><vr>
  Simulated Program Output<br>
  ![image](https://user-images.githubusercontent.com/66567559/178666002-6a9479da-3a2c-469a-a3e5-c1e885eb41b4.png)
<br><br>
Analysis:<br>
Initially, among the five processes, process with ID:5 is the one with the highest ID, so it is selected as
a leader. After that, the process with ID:5 crashes and since process with ID:4 is dead, process with
ID:3 is selected as leader. After some time, the process with ID:4 activates and calls for election. Since,
process with ID:5 is dead, the process with ID:4 is selected as leader. 
<br><br>
  🔶<b> Ring Algorithm </b> <br><br>
  This algorithm applies to systems organized as a ring (logically or physically). In this algorithm,
we assume that the links between the processes are unidirectional and that every process can
message the process on its right only. <br><br>
  Simulated Program Output<br>
  ![444](https://user-images.githubusercontent.com/66567559/178669266-d7be0e4d-087c-49a6-ad47-405ba86ebe42.jpg)
  <br><br>
------------------------------------------------------------------------------------------------------------------------------<br>
  
  Thank You...
  
  
