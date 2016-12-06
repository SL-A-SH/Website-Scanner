from general import *
from domain_name import *
from ip_address import *
from nmap import *
from whois import *
from robots_txt import *

ROOT_DIR = 'websites'
create_dir(ROOT_DIR)

def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F' , ip_address)
    robots = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots, whois)

def create_report(name, full_url, domain_name, nmap, robots, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots.txt', robots)
    write_file(project_dir + '/whois.txt', whois)

gather_info('google', 'https://www.google.com/')


