#!/usr/bin/env python3
import argparse, os, re
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
def main():
  ap=argparse.ArgumentParser(); ap.add_argument("--summary",required=True); ap.add_argument("--out",required=True); ap.add_argument("--fail-on-missing",action="store_true"); a=ap.parse_args()
  sd=os.path.dirname(os.path.normpath(a.summary))
  md=[]
  for line in open(a.summary,encoding="utf-8"):
    m=LINK_RE.search(line);
    if not m: continue
    link=m.group(1).split("#",1)[0].strip()
    if link.startswith("http://") or link.startswith("https://"): continue
    if not (link.endswith(".md") or link.endswith(".markdown")): continue
    md.append(os.path.normpath(os.path.join(sd,link)))
  ordered=[]; seen=set()
  for p in md:
    if p in seen: continue
    seen.add(p); ordered.append(p)
  missing=[p for p in ordered if not os.path.exists(p)]
  if missing and a.fail_on_missing: raise SystemExit("Missing referenced Markdown files:\n"+"\n".join(missing))
  out=[]
  for p in ordered:
    if not os.path.exists(p): out.append(f"\n\n<!-- MISSING: {p} -->\n\n"); continue
    out.append(open(p,encoding="utf-8").read().rstrip()+"\n\n")
  open(a.out,"w",encoding="utf-8").write("".join(out).strip()+"\n")
  print(f"Assembled {len(ordered)} files into {a.out}")
if __name__=="__main__": main()