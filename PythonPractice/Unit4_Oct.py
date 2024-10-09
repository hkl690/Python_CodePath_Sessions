#prompt = input('Please enter a word: ')
#print(prompt)


# Unit 4 Standard 1
# Problem 1: NFT Name Extractor
# You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs from a given list of dictionaries. Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.
# Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

# Problem 2: NFT Collection Review
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

# Problem 3: Identify Popular Creators
# You have been tasked with identifying the most popular NFT creators in your collection. A creator is considered "popular" if they have created more than one NFT in the collection.
# Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.

def identify_popular_creators(nft_collection):
    creator_count = {}

    for nft in nft_collection:
        creator = nft["creator"]
        if creator in creator_count:
            creator_count[creator] += 1
        else:
            creator_count[creator] = 1

    pop_creators = [creator for creator, count in creator_count.items() if count > 1]
    return pop_creators

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3)) # empty
