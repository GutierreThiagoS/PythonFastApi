import uvicorn
from fastapi import FastAPI

from app.models.item import Item, RequestProducts, ResponseProducts, Product

app = FastAPI()

print("API Rodando")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}


@app.get("/revistas")
async def get_all_re():
    return (
        {
            "revistas": [
                "../images/revistas/201902-FEVEREIRO_2019.jpg", "../images/revistas/201902-FEVEREIRO_2019.pdf",
                "../images/revistas/201903-MARCO_2019.jpg", "../images/revistas/201903-MARCO_2019.pdf",
                "../images/revistas/201904-ABRIL_2019.jpg", "../images/revistas/201904-ABRIL_2019.pdf",
                "../images/revistas/201905-MAIO_2019.jpg", "../images/revistas/201905-MAIO_2019.pdf",
                "../images/revistas/201906-JUNHO_2019.pdf", "../images/revistas/201906-JUNHO_2019.png",
                "../images/revistas/201907-JULHO_2019.pdf", "../images/revistas/201907-JULHO_2019.png",
                "../images/revistas/201908-AGOSTO_2019.jpg", "../images/revistas/201908-AGOSTO_2019.pdf",
                "../images/revistas/201909-SETEMBRO_2019.jpg", "../images/revistas/201909-SETEMBRO_2019.pdf",
                "../images/revistas/201910-OUTUBRO_2019.jpg", "../images/revistas/201910-OUTUBRO_2019.pdf",
                "../images/revistas/201911-NOVEMBRO_2019.jpg", "../images/revistas/201911-NOVEMBRO_2019.pdf",
                "../images/revistas/202002-FEVEREIRO_2020.jpg", "../images/revistas/202002-FEVEREIRO_2020.pdf",
                "../images/revistas/202003-MARCO_2020.png", "../images/revistas/202008-AGOSTO_2020.jpg",
                "../images/revistas/202008-AGOSTO_2020.pdf", "../images/revistas/202009-SETEMBRO_2020.jpg",
                "../images/revistas/202009-SETEMBRO_2020.pdf", "../images/revistas/202010-OUTUBRO_2020.pdf",
                "../images/revistas/202010-OUTUBRO_2020.png", "../images/revistas/202011-NOVEMBRO_2020.pdf",
                "../images/revistas/202011-NOVEMBRO_2020.png", "../images/revistas/202012-DEZEMBRO_2020.pdf",
                "../images/revistas/202012-DEZEMBRO_2020.png", "../images/revistas/202101-JANEIRO_2021.jpg",
                "../images/revistas/202101-JANEIRO_2021.pdf", "../images/revistas/202102-FEVEREIRO_2021.jpg",
                "../images/revistas/202102-FEVEREIRO_2021.pdf", "../images/revistas/202103-MARCO_2021.jpg",
                "../images/revistas/202103-MARCO_2021.pdf", "../images/revistas/202104-ABRIL_2021.jpg",
                "../images/revistas/202104-ABRIL_2021.pdf", "../images/revistas/202105-MAIO_2021.jpg",
                "../images/revistas/202105-MAIO_2021.pdf", "../images/revistas/202106-JUNHO_2021.jpg",
                "../images/revistas/202106-JUNHO_2021.pdf", "../images/revistas/202107-JULHO_2021.jpg",
                "../images/revistas/202107-JULHO_2021.pdf", "../images/revistas/202108-AGOSTO_2021.jpg",
                "../images/revistas/202108-AGOSTO_2021.pdf", "../images/revistas/202109-SETEMBRO_2021.jpg",
                "../images/revistas/202109-SETEMBRO_2021.pdf", "../images/revistas/202110-OUTUBRO_2021.jpg",
                "../images/revistas/202110-OUTUBRO_2021.pdf", "../images/revistas/202111-NOVEMBRO_2021.jpg",
                "../images/revistas/202111-NOVEMBRO_2021.pdf", "../images/revistas/202112-DEZEMBRO_2021.jpg",
                "../images/revistas/202112-DEZEMBRO_2021.pdf", "../images/revistas/202201-JANEIRO_2022.jpg",
                "../images/revistas/202201-JANEIRO_2022.pdf", "../images/revistas/202202-FEVEREIRO_2022.jpg",
                "../images/revistas/202202-FEVEREIRO_2022.pdf", "../images/revistas/202203-MARCO_2022.jpg",
                "../images/revistas/202203-MARCO_2022.pdf", "../images/revistas/202204-ABRIL_2022.jpg",
                "../images/revistas/202204-ABRIL_2022.pdf", "../images/revistas/202205-MAIO_2022.jpg",
                "../images/revistas/202205-MAIO_2022.pdf", "../images/revistas/202206-JUNHO_2022.jpg",
                "../images/revistas/202206-JUNHO_2022.pdf", "../images/revistas/202207-JULHO_2022.jpg",
                "../images/revistas/202207-JULHO_2022.pdf", "../images/revistas/202208-AGOSTO_2022.jpg",
                "../images/revistas/202208-AGOSTO_2022.pdf", "../images/revistas/202211-NOVEMBRO_2022.jpg",
                "../images/revistas/202211-NOVEMBRO_2022.pdf", "../images/revistas/202301-JANEIRO_2023.jpg",
                "../images/revistas/202301-JANEIRO_2023.pdf", "../images/revistas/202302-FEVEREIRO_2023.jpg",
                "../images/revistas/202302-FEVEREIRO_2023.pdf", "../images/revistas/202303-MARCO_2023.jpg",
                "../images/revistas/202303-MARCO_2023.pdf", "../images/revistas/202304-ABRIL_2023.jpg",
                "../images/revistas/202304-ABRIL_2023.pdf", "../images/revistas/202305-MAIO_2023.jpg",
                "../images/revistas/202305-MAIO_2023.pdf", "../images/revistas/202306-JUNHO_2023.jpg",
                "../images/revistas/202306-JUNHO_2023.pdf", "../images/revistas/202307-JULHO_2023.jpg",
                "../images/revistas/202307-JULHO_2023.pdf", "../images/revistas/202308-AGOSTO_2023.jpg",
                "../images/revistas/202308-AGOSTO_2023.pdf", "../images/revistas/202309-SETEMBRO_2023.jpg",
                "../images/revistas/202309-SETEMBRO_2023.pdf", "../images/revistas/202310-OUTUBRO_2023.jpg",
                "../images/revistas/202310-OUTUBRO_2023.pdf", "../images/revistas/202311-NOVEMBRO_2023.jpg",
                "../images/revistas/202311-NOVEMBRO_2023.pdf", "../images/revistas/202312-DEZEMBRO_2023.jpg",
                "../images/revistas/202312-DEZEMBRO_2023.pdf", "../images/revistas/202401-JANEIRO_2024.jpg",
                "../images/revistas/202401-JANEIRO_2024.pdf", "../images/revistas/202402-FEVEREIRO_2024.jpg",
                "../images/revistas/202402-FEVEREIRO_2024.pdf", "../images/revistas/202403-MARCO_2024.jpg",
                "../images/revistas/202403-MARCO_2024.pdf", "../images/revistas/202404-ABRIL_2024.jpg",
                "../images/revistas/202404-ABRIL_2024.pdf", "../images/revistas/202405-MAIO_2024.jpg",
                "../images/revistas/202405-MAIO_2024.pdf", "../images/revistas/202406-JUNHO_2024.jpg",
                "../images/revistas/202406-JUNHO_2024.pdf", "../images/revistas/Thumbs.db"
            ]
        }
    )


@app.post("/products")
def get_products(item: RequestProducts):
    print(item)
    return ResponseProducts(
        products=[
            Product(
                description="Teste 1",
                image=""
            ),
            Product(
                description="Teste 2",
                image=""
            )
        ]
    )


if __name__ == "__main__":
    uvicorn.run(app, host="192.168.203.56", port=8443)
