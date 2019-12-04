import csv
import json

desktop = "C:\\Users\\Sam\\Desktop\\"

# """MT数据"""
# mt_dict = dict()
# with open(f"{desktop}EURUSD Filtered ticks 2019112706-2806.csv", "r") as mt_boj:
#     mt_content = csv.reader(mt_boj)
#     with open(f"{desktop}EURUSD_mt_new.csv", "a", newline="") as new_mt_obj:
#         data = csv.writer(new_mt_obj)
#         for line in mt_content:
#             if mt_dict.get(line[0]) is None:
#                 mt_dict[line[0]] = dict()
#
#                 mt_dict[line[0]]["bid"] = []
#                 mt_dict[line[0]]["bid"].append(float("%.5f" % float(line[1])))
#
#                 mt_dict[line[0]]["ask"] = []
#                 mt_dict[line[0]]["ask"].append(float("%.5f" % float(line[2])))
#             else:
#                 mt_dict[line[0]]["bid"] += [(float("%.5f" % float(line[1])))]
#                 mt_dict[line[0]]["ask"] += [(float("%.5f" % float(line[2])))]
#
#             data.writerow([
#                 line[0],
#                 json.dumps(mt_dict[line[0]])
#             ])
#
# """MongoDB数据"""
# md_dict = dict()
# with open(f"{desktop}142-3.csv", "r") as md_boj:
#     md_content = csv.reader(md_boj)
#     with open(f"{desktop}EURUSD_md_new.csv", "a", newline="") as new_md_obj:
#         data = csv.writer(new_md_obj)
#         for line in md_content:
#             key = line[0][:-1].replace("-", ".")
#             if md_dict.get(key) is None:
#                 md_dict[key] = dict()
#
#                 md_dict[key]["bid"] = []
#                 md_dict[key]["bid"].append(float("%.5f" % float(line[1])))
#
#                 md_dict[key]["ask"] = []
#                 md_dict[key]["ask"].append(float("%.5f" % float(line[2])))
#             else:
#                 md_dict[key]["bid"] += [(float("%.5f" % float(line[1])))]
#                 md_dict[key]["ask"] += [(float("%.5f" % float(line[2])))]
#
#             data.writerow([
#                 key,
#                 json.dumps(md_dict[key])
#             ])


# with open(f"{desktop}EURUSD_mt_new.csv", "r") as r_mt_obj:
#     r_mt_content = csv.reader(r_mt_obj)
#     with open(f"{desktop}EURUSD_mt_new_new.csv", "a", newline='') as w_mt_obj:
#         w_mt_data = csv.writer(w_mt_obj)
#         for line in r_mt_content:
#             ba = json.loads(line[1])
#             bid = round(sum(ba["bid"]) / len(ba["bid"]), 5)
#             ask = round(sum(ba["ask"]) / len(ba["ask"]), 5)
#             w_mt_data.writerow([line[0], bid, ask])

# with open(f"{desktop}EURUSD_md_new.csv", "r") as r_md_obj:
#     r_md_content = csv.reader(r_md_obj)
#     with open(f"{desktop}EURUSD_md_new_new.csv", "a", newline='') as w_md_obj:
#         w_md_data = csv.writer(w_md_obj)
#         for line in r_md_content:
#             ba = json.loads(line[1])
#             bid = round(sum(ba["bid"]) / len(ba["bid"]), 5)
#             ask = round(sum(ba["ask"]) / len(ba["ask"]), 5)
#             w_md_data.writerow([line[0], bid, ask])
