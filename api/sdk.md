# Tài liệu SDK

Chúng tôi cung cấp SDK mẫu để gọi API nhanh. Dưới đây là ví dụ cho Node.js và Python.

## Node.js (ví dụ)
```js
const TriAnh = require('trianh-sdk')
const client = new TriAnh({ apiKey: process.env.TRIANH_API_KEY })
await client.sms.send({ from: 'TRIANH', to: ['849...'], message: 'Hello' })
```

## Python (ví dụ)
```py
from trianh import TriAnh
client = TriAnh(api_key=os.getenv('TRIANH_API_KEY'))
client.sms.send(from='TRIANH', to=['849...'], message='Hello')
```

---
[Previous](../api/overview.md) • [Next](../support.md)
