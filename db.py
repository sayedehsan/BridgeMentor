from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://28b9r42LvvoWwRC.root:Yy1KA7vFD58ztFKo@gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com:4000/test?ssl_ca=<CA_PATH>&ssl_verify_cert=true&ssl_verify_identity=true"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping = True,
    connect_args = {
        "ssl" :{
            "ssl": True
        }
    } 
)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
