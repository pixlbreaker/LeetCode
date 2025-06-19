# Last updated: 6/18/2025, 11:11:46 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        return address.replace(".", "[.]")