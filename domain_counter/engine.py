from collections import Counter


def read_file(file_path: str) -> list:
    return [item.strip() for item in open(file_path)]


def is_not_corrent_domain(domain: str) -> bool:
    return len(domain.split("@")) != 2


def domain_count(domains: list) -> Counter:
    domain_count_dict = Counter()  # type: Counter
    for item in domains:
        if is_not_corrent_domain(item):
            domain = "INVALID"
        else:
            domain = item.split("@")[1]
        domain_count_dict[domain] = domain_count_dict[domain] + 1
    return domain_count_dict


def show_result(domain_count: Counter) -> None:
    # 'INVALID' on the last line
    sorted_domain_count = sorted(
        domain_count.items(),
        key=lambda x: (x[0] != "INVALID", x[1]),
        reverse=True,
    )
    for domain, num_count in sorted_domain_count:
        print(f"{domain}\t{num_count}")


def make_result(file_path) -> None:
    domain_list = read_file(file_path)
    result = domain_count(domains=domain_list)
    show_result(result)
