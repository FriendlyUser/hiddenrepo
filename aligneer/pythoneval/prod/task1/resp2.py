import tenseal as ts

def encrypt_vector(vector, context):
    return ts.ckks_vector(context, vector)

def encrypted_dot_product(enc_vec1, enc_vec2):
    return enc_vec1.dot(enc_vec2)

# Create a TenSEAL context with proper parameters
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set the scale (this is crucial for CKKS)
context.global_scale = 2**40

# Generate keys
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

# Calculate expected result for verification
expected_result = sum(a * b for a, b in zip(vector_a, vector_b))

print("Encrypted dot product result:", decrypted_result)
print("Expected result:", expected_result)
