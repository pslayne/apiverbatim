import bcrypt

def hash_password(raw):
    hashed = bcrypt.hashpw(raw.encode(), bcrypt.gensalt())
    return str(hashed)[2:-1]

def check_password(raw, hashed):
    return bcrypt.checkpw(raw.encode(), hashed.encode())
