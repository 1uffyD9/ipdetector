import re

def ipCategorizer(ip):
    ip_pub_match = re.compile("^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))(?<!127)(?<!^10)(?<!^0)\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!192\.168)(?<!172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!\.255$)$")
    ip_priv_match = re.compile("(^192\.168\.([0-9]|[0-9][0-9]|[0-1][0-9][0-9]|[0-2][0-5][0-5])\.([0-9]|[0-9][0-9]|[0-1][0-9][0-9]|[0-2][0-5][0-5])$)|(^172\.([1][6-9]|[2][0-9]|[3][0-1])\.([0-9]|[0-9][0-9]|[0-1][0-9][0-9]|[0-2][0-5][0-5])\.([0-9]|[0-9][0-9]|[0-1][0-9][0-9]|[0-2][0-5][0-5])$)|(^10\.([0-9]|[0-9][0-9]|[0-1][0-9][0-9]|[0-2][0-5][0-5])\.([0-9]|[0-9][0-9]|[0-1][0-9][0-9]|[0-2][0-5][0-5])\.([0-9]|[0-9][0-9]|[0-1][0-9][0-9]|[0-2][0-5][0-5])$)")
    ip_pub_range_match = re.compile("^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))(?<!127)(?<!^10)(?<!^0)\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!192\.168)(?<!172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!\.255$)\/([8-9]|[1-2][0-9]|30)$")
    ip_priv_range_match = re.compile("(^192\.168\.([0-9]|[0-9][0-9]|[0-2][0-5][0-5])\.([0-9]|[0-9][0-9]|[0-2][0-5][0-5])\/([8-9]|[1-2][0-9]|30)$)|(^172\.([1][6-9]|[2][0-9]|[3][0-1])\.([0-9]|[0-9][0-9]|[0-2][0-5][0-5])\.([0-9]|[0-9][0-9]|[0-2][0-5][0-5])\/([8-9]|[1-2][0-9]|30)$)|(^10\.([0-9]|[0-9][0-9]|[0-2][0-5][0-5])\.([0-9]|[0-9][0-9]|[0-2][0-5][0-5])\.([0-9]|[0-9][0-9]|[0-2][0-5][0-5])\/([8-9]|[1-2][0-9]|30)$)")
    if ip_priv_match.match(ip):
        return [0, ip]
    elif ip_pub_match.match(ip):
        return [1, ip]
    else:
        if ip_priv_range_match.match(ip):
            return [2, ip]
        elif ip_pub_range_match.match(ip):
            return [3, ip]
        else:
            return False