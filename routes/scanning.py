
from fastapi import APIRouter

from database import SessionDep

router = APIRouter(prefix="/api/v1", tags=["scanning"])


@router.post("/scan")
def scan(session: SessionDep):
    return None


@router.get("/result")
def scan(session: SessionDep, scan_id): # scanid is uuidv4 iirc
    return None

# screenshots missing

# dom missing

# responses filehash missing

# put visibility missing

# delete scan

# get countries

# get user agents

# @router.get("/")
# def scan(session: SessionDep, scan_id): # scanid is uuidv4 iirc
#     return None


