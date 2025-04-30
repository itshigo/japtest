def main():
    import sys

    def test(lines, index, N, results):
        if N == 0:
            return results

        if index >= len(lines) - 1:
            return results + ["-1"]

        try:
            x = int(lines[index])
            nums = list(map(int, lines[index + 1].split()))
            if len(nums) != x:
                return test(lines, index + 2, N - 1, results + ["-1"])
            else:
                def calc_power4(lst):
                    if not lst:
                        return 0
                    head, *tail = lst
                    if head < 0:
                        return head ** 4 + calc_power4(tail)
                    else:
                        return calc_power4(tail)
                total = calc_power4(nums)
                return test(lines, index + 2, N- 1, results + [str(total)])
        except:
            return test(lines, index + 2, N - 1, results + ["-1"])

    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    try:
        N = int(input_data[0])
        results = test(input_data, 1, N , [])
        print('\n'.join(results))
    except:
        pass


if __name__ == "__main__":
    main()
