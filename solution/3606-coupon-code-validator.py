class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        n = len(code)
        valid_coupons = []

        def is_code_valid(code: str) -> bool:
            return len(code) and code.isalnum() or "_" in code

        def is_business_line_valid(business_line: str) -> bool:
            return business_line in ["electronics", "grocery", "pharmacy", "restaurant"]

        def is_active_valid(is_active: bool) -> bool:
            return is_active

        for i in range(n):
            c, bl, ia = code[i], businessLine[i], isActive[i]

            if is_code_valid(c) and is_business_line_valid(bl) and is_active_valid(ia):
                valid_coupons.append([c, bl])

        return list(
            map(lambda x: x[0], sorted(valid_coupons, key=lambda x: (x[1], x[0])))
        )
