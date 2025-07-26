🔹 1. List (Built-in Python Type)
✅ Can hold any data type (integers, strings, objects, etc.)

✅ Dynamic: Can change size and hold mixed data types.

❌ Slower for numerical operations compared to arrays.

✅ Comes built-in; no import needed


2. Array (from array module)
✅ More memory-efficient than lists for large numeric data.

❌ Can only hold elements of the same type.

✅ Faster than lists for numerical operations, but much less used than NumPy arrays for this purpose.

❗ Must import from array module:
from array import array
my_array = array('i', [1, 2, 3, 4])  # 'i' = integer type code


NumPy Array (Recommended for Numeric Work)
✅ Much faster and more efficient than lists or array.array for numerical tasks.

✅ Supports vectorized operations, broadcasting, and more.

❗ Requires NumPy library:

python
Copy
Edit
import numpy as np
np_array = np.array([1, 2, 3, 4])
