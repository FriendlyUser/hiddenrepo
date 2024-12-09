I’m working with the TenSeal library to perform a homomorphically encrypted dot product of two vectors using CKKS encryption. Specifically, I want to compute the dot product of `[1.0, 2.0, 3.0]` and `[4.0, 5.0, 6.0]` entirely in the encrypted domain, and then decrypt the result to verify correctness.

However, my current code is failing with a `ValueError: no global scale`. I suspect I’m not correctly setting the CKKS context or parameters needed for encrypted operations. Could you help identify the issue, correct the code, and explain what was changed and why? In your answer, please provide:

1. A corrected version of the code that properly sets up the TenSeal context, encrypts the vectors, performs the encrypted dot product, and decrypts the result without errors.
2. A clear explanation of the modifications made, especially regarding the CKKS context and any necessary scaling parameters.

Here’s my original code snippet and the error message I’m receiving:

**Original Code:**
```python
import tenseal as ts

def encrypt_vector(vector, context):
    return ts.ckks_vector(context, vector)

def encrypted_dot_product(enc_vec1, enc_vec2):
    return enc_vec1.dot(enc_vec2)

# Create a TenSEAL context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.generate_galois_keys()

# Original vectors
vector_a = [1.0, 2.0, 3.0]
vector_b = [4.0, 5.0, 6.0]

# Encrypt the vectors
enc_vector_a = encrypt_vector(vector_a, context)
enc_vector_b = encrypt_vector(vector_b, context)

# Compute the encrypted dot product
enc_result = encrypted_dot_product(enc_vector_a, enc_vector_b)

# Decrypt the result
decrypted_result = enc_result.decrypt()[0]

print("Encrypted dot product result:", decrypted_result)
```

**Error Message:**
```
ValueError: no global scale
```

Please show me a working version of the code and explain what changed.