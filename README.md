# Guardian Articles Crawler

It is running on http://ec2-52-65-4-70.ap-southeast-2.compute.amazonaws.com/

The API to search is http://ec2-52-65-4-70.ap-southeast-2.compute.amazonaws.com/search?query=<keywords>

The response is like 

```json
[
  {
    "author": "Rosanna Greenstreet",
    "cacheDateTime": "Sun, 07 Aug 2016 23:44:29 GMT",
    "headline": "Isla Fisher: My guiltiest pleasure? Following Justin Bieber on Instagram",
    "imageUrl": "https://i.guim.co.uk/img/media/53903f85ec997607b34a8513572f12431b07a28b/0_28_1762_1056/master/1762.jpg?w=300&q=55&auto=format&usm=12&fit=max&s=2ec4146bc7c8d18d1c4aad7756f08f5f",
    "url": "https://www.theguardian.com/lifeandstyle/2016/jul/30/isla-fisher-q-and-a-justin-bieber"
  },
  {
    "author": "Rob Davies",
    "cacheDateTime": "Sun, 07 Aug 2016 23:44:54 GMT",
    "headline": "Uber bows out of China fray with lots of fight left for dominance elsewhere",
    "imageUrl": "https://i.guim.co.uk/img/media/94af0e5209fedce165d486e944de238dcfa6205b/0_190_3039_1823/master/3039.jpg?w=300&q=55&auto=format&usm=12&fit=max&s=94a2d7cb41d4eab89185c02073ac23a1",
    "url": "https://www.theguardian.com/technology/2016/aug/06/uber-chinese-deal-ride-sharing-india-taxis"
  }
]

```
