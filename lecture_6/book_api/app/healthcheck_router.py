from fastapi import APIRouter, status

router = APIRouter(
    tags=["Healthcheck"]
)

# Healthcheck
@router.get("/healthcheck", status_code= status.HTTP_200_OK)
async  def healthcheck():
    return {"status": "ok"}