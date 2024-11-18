

from wb_func_p2 import get_sub_cat_urls, cat_collector

if __name__=="__main__":
    remove_dict = {
        "__seller.wildberries.ru": "https://seller.wildberries.ru/", "trudoustroystvo__services": "https://www.wildberries.ru/services/trudoustroystvo", "chernaya-pyatnitsa__promotions": "https://www.wildberries.ru/promotions/chernaya-pyatnitsa", "certificates__gift": "https://www.wildberries.ru/gift/certificates", "trend__promotions": "https://www.wildberries.ru/promotions/trend", "ekspress-dostavka__catalog": "https://www.wildberries.ru/catalog/ekspress-dostavka", "dobroshrift__promotions": "https://www.wildberries.ru/promotions/dobroshrift", "zhenshchinam__catalog": "https://www.wildberries.ru/catalog/zhenshchinam", "obuv__catalog": "https://www.wildberries.ru/catalog/obuv", "detyam__catalog": "https://www.wildberries.ru/catalog/detyam", "muzhchinam__catalog": "https://www.wildberries.ru/catalog/muzhchinam", "dom-i-dacha__catalog": "https://www.wildberries.ru/catalog/dom-i-dacha", "krasota__catalog": "https://www.wildberries.ru/catalog/krasota", "aksessuary__catalog": "https://www.wildberries.ru/catalog/aksessuary", "elektronika__catalog": "https://www.wildberries.ru/catalog/elektronika", "igrushki__catalog": "https://www.wildberries.ru/catalog/igrushki", "mebel__dom": "https://www.wildberries.ru/catalog/dom/mebel", "tovary-dlya-vzroslyh__aksessuary": "https://www.wildberries.ru/catalog/aksessuary/tovary-dlya-vzroslyh", "pitanie__catalog": "https://www.wildberries.ru/catalog/pitanie", "tsvety__catalog": "https://www.wildberries.ru/catalog/tsvety", "bytovaya-tehnika__catalog": "https://www.wildberries.ru/catalog/bytovaya-tehnika", "tovary-dlya-zhivotnyh__catalog": "https://www.wildberries.ru/catalog/tovary-dlya-zhivotnyh", "sport__catalog": "https://www.wildberries.ru/catalog/sport", "avtotovary__aksessuary": "https://www.wildberries.ru/catalog/aksessuary/avtotovary", "transportnye-sredstva__catalog": "https://www.wildberries.ru/catalog/transportnye-sredstva", "knigi__catalog": "https://www.wildberries.ru/catalog/knigi", "yuvelirnye-ukrasheniya__catalog": "https://www.wildberries.ru/catalog/yuvelirnye-ukrasheniya", "instrumenty__dom-i-dacha": "https://www.wildberries.ru/catalog/dom-i-dacha/instrumenty", "dachniy-sezon__catalog": "https://www.wildberries.ru/catalog/dachniy-sezon", "zdorove__dom-i-dacha": "https://www.wildberries.ru/catalog/dom-i-dacha/zdorove", "kantstovary__knigi-i-diski": "https://www.wildberries.ru/catalog/knigi-i-diski/kantstovary", "kulturnyy-kod__catalog": "https://www.wildberries.ru/catalog/kulturnyy-kod", "promotions__www.wildberries.ru": "https://www.wildberries.ru/promotions", "__digital.wildberries.ru": "https://digital.wildberries.ru/", "__vmeste.wildberries.ru": "https://vmeste.wildberries.ru/", "lk__www.wildberries.ru": "https://www.wildberries.ru/lk", "delivery__myorders": "https://www.wildberries.ru/lk/myorders/delivery", "archive__myorders": "https://www.wildberries.ru/lk/myorders/archive", "get__receipts": "https://www.wildberries.ru/lk/receipts/get", "myrefunds__lk": "https://www.wildberries.ru/lk/myrefunds", "favorites__lk": "https://www.wildberries.ru/lk/favorites", "favoritebrands__lk": "https://www.wildberries.ru/lk/favoritebrands", "purchases__mywallet": "https://www.wildberries.ru/lk/mywallet/purchases", "feedback__discussion": "https://www.wildberries.ru/lk/discussion/feedback", "feedback?type=waiting_feedbacks__discussion": "https://www.wildberries.ru/lk/discussion/feedback?type=waiting_feedbacks", "feedback?type=comments__discussion": "https://www.wildberries.ru/lk/discussion/feedback?type=comments", "feedback?type=questions__discussion": "https://www.wildberries.ru/lk/discussion/feedback?type=questions", "communications__lk": "https://www.wildberries.ru/lk/communications"
    }


    keys_to_remove = [el for el in remove_dict.keys()]
    sub_cat_dict = get_sub_cat_urls()
    for key in keys_to_remove:
        sub_cat_dict.pop(key, None)
    cat_collector(sub_cat_dict)




    #sun_cat_dict = get_sub_cat_urls()
    #A = {"": "https://digital.wildberries.ru/", "trudoustroystvo": "https://www.wildberries.ru/services/trudoustroystvo", "chernaya-pyatnitsa": "https://www.wildberries.ru/promotions/chernaya-pyatnitsa"}
    #cat_collector(A)
