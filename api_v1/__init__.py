from fastapi import APIRouter

from .product.views import router as products_router
from .post.views import router as post_router
from .auth.views import router as auth_router

router = APIRouter()

router.include_router(router=auth_router, prefix="/auth")
router.include_router(router=products_router, prefix="/product")
router.include_router(router=post_router, prefix="/post")
