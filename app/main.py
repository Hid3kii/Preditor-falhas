from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app.models.base import Base
from app.models import Host, Medicao
from app.schemas.host import HostCreate
from app.schemas.medicao import MedicaoCreate
from app.models.medicao import Medicao

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

@app.post("/medicoes")
def criar_medicao(medicao: MedicaoCreate, db: Session = Depends(get_db)):
    nova_medicao = Medicao(
        host_id=medicao.host_id,
        latencia_ms=medicao.latencia_ms,
        perda_pacotes=medicao.perda_pacotes,      
        status="ok"
    )

    db.add(nova_medicao)
    db.commit()
    db.refresh(nova_medicao)

    return nova_medicao

@app.get("/hosts/{host_id}/medicoes")
def listar_medicoes(host_id: int, db: Session = Depends(get_db)):
    medicoes = db.query(Medicao).filter(
        Medicao.host_id == host_id
    ).all()

    return medicoes