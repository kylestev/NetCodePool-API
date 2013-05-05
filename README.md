NetCodePool-API
===============

### Examples
```python
import api

net = NetCodePoolAPI('API-KEY-HERE')
net.refresh()

print 'Alive workers:', [k for k, v in net.get_workers().items() if v['alive']]
print 'Best hashrate:', max([v['hashrate'] for k, v in net.get_workers().items()])
print 'Round earnings estimate:', net.get_stat('estimate')
print 'Current total hashrate:', net.get_stat('hashrate')
```
