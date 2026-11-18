
import os
import sqlite3
from typing import Literal
from pathlib import Path
import bcrypt

# Caminho seguro para o DB (pode ser configurado via variável de ambiente)
DB_PATH = Path(os.getenv("DIO_DB_PATH", "/home/ryan-soares/Documents/Repos/dio-agent/database.db"))


def _hash_password(plain: str) -> bytes:
    """Gera um hash bcrypt a partir da senha em texto‑plano."""
    return bcrypt.hashpw(plain.encode("utf-8"), bcrypt.gensalt())


def _verify_password(plain: str, hashed: bytes) -> bool:
    """Compara senha em texto‑plano com hash armazenado."""
    return bcrypt.checkpw(plain.encode("utf-8"), hashed)


def login_db(user: str, password: str) -> Literal["access allowed", "access denied"]:
    """Autentica usuário usando consultas parametrizadas e senhas hash.

    Retorna "access allowed" caso o usuário exista e a senha corresponda.
    """
    if not (user and password):
        return "access denied"

    try:
        # Conexão usando caminho absoluto e modo de leitura/escrita controlado
        conn = sqlite3.connect(str(DB_PATH))
        cur = conn.cursor()

        # Consulta parametrizada para evitar SQL injection
        cur.execute(
            "SELECT password FROM users WHERE username = ?",
            (user,)
        )
        row = cur.fetchone()
        if row and _verify_password(password, row[0].encode()):
            result = "access allowed"
        else:
            result = "access denied"
    except sqlite3.Error as e:
        # Log interno (não expõe detalhes ao cliente)
        # Por exemplo, usar logging module (omitted aqui por brevidade)
        result = "access denied"
    finally:
        conn.close()

    return result