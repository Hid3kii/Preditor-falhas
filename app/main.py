from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app.models.base import Base
from app.models import Host, Medicao
from app.schemas.host import HostCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/hosts")
def criar_host(host: HostCreate, db: Session = Depends(get_db)):
    novo_host = Host(
        nome=host.nome,
        endereco_ip=host.endereco_ip
    )

    db.add(novo_host)
    db.commit()
    db.refresh(novo_host)

    return novo_host

@app.get("/hosts")
def listar_hosts(db: Session = Depends(get_db)):
    hosts = db.query(Host).all()

    return hosts