Согласно теореме CAP к какой части вы можете отнести СУБД:  
- DragonFly  
- ScyllaDB  
- ArenadataDB

#### Dragonfly  
На сайте DragonFly написано:  
> High Availability  
Dragonfly natively supports an eventually consistent primary-replica model to achieve high availability. If an outage on the primary occurs, Dragonfly will automatically failover to the replica and promote it as the primary.  

Значит ее можно отнести к AP.  

#### ScyllaDB  
В документации сказано, что ScyllaDB относится к AP.  
[ссылка](https://opensource.docs.scylladb.com/stable/architecture/architecture-fault-tolerance.html)  

#### ArenadataDB

Относится к CP.  