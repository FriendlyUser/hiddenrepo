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

# Set the global scale
context.global_scale = 2**40

# Generate Galois keys for rotation operations (needed for dot product)
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