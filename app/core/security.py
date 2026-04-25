import bcrypt
from jose import jwt
from datetime import datetime, timedelta, timezone
import os

# 加载环境变量
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


class PasswordHelper:
    @staticmethod
    def hash_password(password: str) -> str:
        # 确保截断到 72 字节并编码
        pwd_bytes = password[:72].encode("utf-8")
        # gensalt() 默认包含随机盐，强度足够
        hashed = bcrypt.hashpw(pwd_bytes, bcrypt.gensalt())
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        # 修正拼写错误：checkpw
        try:
            return bcrypt.checkpw(
                plain_password[:72].encode("utf-8"),
                hashed_password.encode("utf-8")
            )
        except Exception:
            return False


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    生成 JWT 访问令牌
    :param data: 存入 payload 的数据（sub, role）
    :param expires_delta: 过期时长
    :return: 签名后的 Token 字符串
    """
    to_encode = data.copy()

    # 使用 timezone.utc 避免本地时间偏移风险
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=60)

    to_encode.update({"exp": expire})

    # 调用 jwt.encode。信安建议：确保 ALGORITHM 是在代码或环境变量中写死的，不接受客户端传参
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt