[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# February 2026

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/title.png)

*History is supposed to repeat itself. Usually, we look back at the past year to how our plans unfolded and developed and try to learn from that, to see what we can do differently this year. This of course, assumes that the coming year will be the same as the year the passed. The same patterns, people, and processes that we've already seen. It looks like this is no longer the case though, at least in our industry. Every year it seems things change faster than we can keep up with. Patterns we saw in markets or technology don't repeat, each development or hurdle seems to be completely new and unpredictable, and in this case, what should one do? To know how to best act in the future, do we still study history, or actively strive to forget it?*

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top of everything, or even summarising all the material available can be difficult - so we do it for you.

For a space to share sources and news/updates, join our telegram channel <a href="https://t.me/aihpc_infra_fans">here</a> or if you like short form posts on similar topics, check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar-6ru/>LinkedIn</a>.

[**This month's updates:**]

- [**ZAM**]
- [**Meta goes all-in on NVIDIA**]
- [**HBM news**]
- [**Other notable headlines**]

---

# This month's updates

## ZAM

HBM (as we know it) appears to be reaching some physical limits, and even though experts forecast continuous improvement up to 2038, others are working on a new approach that promises progress sooner.

![HBM roadmap](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_hbm_roadmap.png)

*Source: KAIST teralabs*

Z-Angle Memory, or ZAM, is a next-generation vertically-stacked DRAM technology designed to compete with HBM in future hardware that will require large volumes of on-device, high-bandwidth memory. Basically, GPUs, TPUs, and whatever other PUs will aim for AI training and bandwidth-intensive inference workloads. ZAM differs from HBM in a few key ways that we'll detail shortly, but the most apparent is that the DRAM dies stand upright, rather than laying flat horizontally as in HBM.

![ZAM architecture](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_architecture.png)

*Source: SemiVision*

Stacking dies horizontally works great to increase capacity and bandwidth in a small volume, but it comes with 

![HBM TSVs](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_hbm.jpeg)

*Source: Block and Files*

ZAM = Z-Angle Memory, a next-generation vertically-stacked DRAM technology designed to compete with (and potentially displace) HBM in AI/HPC datacenter workloads.
The "Z-Angle" name refers to a staggered interconnect topology that routes connections diagonally within the die stack, rather than drilling straight down via traditional TSVs (Through-Silicon Vias) as used in HBM. Tom's Hardware
ZAM uses a single central channel to deliver power and signals, replacing HBM's "honeycomb TSV mesh" with a single-axis structure. Eight wafers containing the novel NGDB DRAM architecture are vertically bonded on a base wafer and connected using an alternative "via-in-one" construct. Substack
ZAM utilises copper-to-copper (Cu-Cu) hybrid bonding, creating a monolithic-like silicon block that significantly reduces the vertical height of the stack while improving thermal conductivity. FinancialContent
Intel's Embedded Multi-Die Interconnect Bridge (EMIB) is used to reduce latency between the individual stacked chips, and would connect the memory to the AI accelerator. Tom's Hardware

Why does ZAM exist? (The problem it solves)

Traditional memory uses a planar stacked structure that is reaching its limits due to power and heat constraints. Current designs have pushed 16 layers close to the maximum, with 20 layers considered the upper limit. TrendForce
HBM stacks rely on thousands of TSVs per die that consume valuable silicon area, reduce effective memory density, weaken wafer mechanical integrity, and increase warpage risk. As stack layers increase (12-Hi, 16-Hi and beyond), middle dies become thermal dead zones where heat generated must pass through multiple low-conductivity layers, creating thermal gradients and hot spots. Substack
Memory bandwidth is currently a major bottleneck in AI processing. Surging HBM demand has led to a global shortage in NAND stocks, pushing up prices and creating supply chain shortages. HPCwire
HBM often trades improved bandwidth for lower performance in other areas, like capacity. The NGDB initiative aims to remove this tradeoff, bridging the gap between HBM and conventional DDR DRAM while delivering significantly better energy efficiency. TrendForce

Claimed performance targets vs HBM

Capacity: Up to 512 GB per chip — 2x to 3x the capacity of current HBM. TrendForce
Power: Energy consumption reduced by 40–50% due to improved thermal regulation and optimised architecture. NEWS.am TECH
Cost: Mass-production costs targeted at around 60% of HBM, per Nikkei reports. TrendForce
Thermal: Vertical die stacking conducts heat from each die upward evenly, addressing thermal challenges that plague planar stacking. The central channel acts like a vertical heat pipe. TrendForce
Manufacturing: Diagonal Z-Angle interconnects are claimed to simplify manufacturing vs TSV-based approaches, potentially improving production yields.

Who is involved? (The consortium)

SAIMEMORY (SoftBank subsidiary): Founded in December 2024, officially launched in June 2025. A joint venture between SoftBank, Intel, and the University of Tokyo. TrendForce Led by President and CEO Hideya Yamaguchi. Responsible for design, IP management, and commercialisation.
Intel: Technology, innovation, and standards partner. Provides stacking architecture and NGDB know-how. This marks Intel's return to the memory market for the first time since the 1980s. Tom's Hardware Intel's role described as "initial investment and strategic decisions."
SoftBank Group: Parent of Saimemory. Capital provider. SoftBank plans to invest roughly ¥3 billion (~$21M) through prototype completion in fiscal 2027. TrendForce Has also invested $2 billion directly in Intel.
PSMC (Powerchip Semiconductor Manufacturing Corp.): Taiwan's PSMC has teamed up in the collaboration, taking on a key role in pilot production and manufacturing. trendforce This gives Taiwan its first real foothold in AI memory manufacturing.
Shinko Electric Industries (Japan): Assists in pilot production and manufacturing / packaging.
Fujitsu: Also involved, contributing along with Japan's RIKEN National Research Institute, ¥1 billion ($7M). Blocks and Files
University of Tokyo: Research partner.
Sandia National Laboratory, Lawrence Livermore National Laboratory, Los Alamos National Laboratory (the "Tri-Lab"): The NGDB program is part of the Advanced Memory Technology (AMT) project, managed by the U.S. Department of Energy and National Nuclear Security Administration (NNSA). The program is currently in its third year — years one and two focused on R&D, year three on productisation. HPCwire

Key people mentioned

Dr. Joshua Fryman — Intel Fellow and CTO of Intel Government Technologies. Presented ZAM at the Japan event.
Makoto Ono — Intel Japan CEO. Co-presented at Intel Connection Japan 2026.
Hideya Yamaguchi — President and CEO of SAIMEMORY.
Gwen Voskuilen — Principal Member of Technical Staff at Sandia National Laboratories. Validated the NGDB approach.

The underlying tech: NGDB (Next Generation DRAM Bonding)

Intel's NGDB initiative was completed under the Advanced Memory Technology (AMT) program managed by the U.S. DOE and NNSA through the Sandia, Lawrence Livermore, and Los Alamos National Laboratories. TweakTown
Intel and Sandia designed a new stacking approach and a different way of organising the DRAM chips. Early prototypes confirmed it was possible to increase capacity through new stacking techniques, and recent developments demonstrated the necessary high performance. Tom's Hardware
NGDB test assemblies consist of eight DRAM wafers vertically bonded on a base wafer, connected using the "via-in-one" construct. Substack
ZAM is described as potentially using a capacitor-less design. Wccftech

Timeline

December 2024: SAIMEMORY incorporated.
Mid-2025: Intel and SoftBank begin building the first prototype, leveraging Intel's packaging technologies and key Japanese patents.
June 2025: SAIMEMORY officially launched.
February 2, 2026: Formal collaboration agreement signed between SAIMEMORY and Intel.
February 3, 2026: First public prototype unveiling at Intel Connection Japan 2026 in Tokyo.
Q1 2026: Operations commence.
FY2027 (by March 31, 2028): Prototype completion target.
FY2029 (2029–2030): Commercial mass production target.

Geopolitical / strategic angle

This is a US-Japan-Taiwan consortium ("friendshoring") explicitly building AI memory supply chains that don't depend on the South Korean memory oligopoly (Samsung, SK hynix) or China. Substack
Japan was a major memory manufacturing region in the 1980s but fell behind with the rise of Korean and Taiwanese manufacturing. SAIMEMORY represents Japan's attempt to re-enter the cutting-edge memory market. Tom's Hardware
Intel exited DRAM in 1985 due to competition from Japanese vendors. This is their return, but now partnering with Japan rather than competing against it. Wccftech Intel once commanded nearly 90% of the global DRAM market (they invented the first commercial DRAM in 1970).
SoftBank's collaboration with Intel on ZAM could allow it to own the memory stack for its own custom ASICs (e.g., the Izanagi lineup), giving greater control over architectural layout. Wccftech
Note: PSMC's Tongluo P5 fab is simultaneously being acquired by Micron for $1.8B (expected to close Q2 2026), adding an interesting wrinkle to the supply chain dynamics.

Market reaction

Intel stock surged 5% overnight while SoftBank rose 3.13% after the announcement. Techbuzz

Competitive context

ZAM will compete against HBM4 (expected from Samsung, SK hynix, Micron in the same timeframe).
Samsung is separately developing zHBM, another alternative approach.
NEO Semiconductor is pursuing a similar non-TSV stacking approach.
Between a stage demonstration and scalable mass production lie packaging hurdles, yield problems, and cost issues. Diagonal interconnects may look elegant but must compete with established TSV processes optimised over many years. HBM has a massive lead in ecosystem, standardisation, and integration into GPU and AI accelerator designs. igor´sLAB

Key risks / scepticism

Still at early prototype stage — proof of concept, not production-ready.
Years of testing, process refinement, and certification ahead before mass production.
Must achieve favourable yield and cost economics at scale.
Needs design wins with accelerator vendors (NVIDIA adoption would be critical).
HBM incumbents are not standing still — HBM4 and HBM5 roadmaps are active.
The 2027 prototype milestone is the key proof point.

## Meta goes all-in on NVIDIA

## HBM news

CPX using HBM3E instead of GDDR7

---

## Other notable headlines

* [InferenceMAX v2 (now called InferenceX) is out - SemiAnalysis](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)
* [NVIDIA pushes Samsung to deliver HBM4 even faster](https://www.chosun.com/economy/tech_it/2026/02/04/I2W4VIHCG5C4XL4Z2EF3X72WDE/)
* [China's HBM3 production is narrowing the gap with South Korea](https://www.mk.co.kr/news/business/11957166)
* [Nvidia's new RTX 6000D appears in teardown: 84GB GDDR7 in China compared to the full 96GB](https://www.tweaktown.com/news/110135/nvidias-new-rtx-6000d-appears-in-teardown-84gb-gddr7-in-china-compared-to-the-full-96gb/index.html)
* [World's first PCIe 6.0 SSD enters mass production with 28GB/s speeds: Micron 9650 series SSDs support air and liquid cooling](https://www.tomshardware.com/pc-components/ssds/worlds-first-pcie-6-0-ssd-enters-mass-production-with-28gb-s-speeds-micron-9650-series-ssds-support-air-and-liquid-cooling)
* [Cisco releases the G300 102.4T switch ASIC](https://mp.weixin.qq.com/s?chksm=e8bf1883dfc89195350bb6dec790d823de6074dac8e9042aa966f21dfca7c113e384fce3d3cb&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1770883821_3&req_id=1770883878521405&mid=2247488461&sn=975a51dd4d8b1c5900c6b59d8ceb81db&idx=1&__biz=MzIyOTcyNzc3Nw%3D%3D&scene=169&subscene=200&sessionid=1770883820)
* [Evercore out with a 4Q25 AI Channel Checks, saying $NVDA Vera Rubin appears to be ahead of schedule (Tweet by @halfblindmonkey)](https://x.com/halfblindmonkey/status/2023737861028098525)
* [Rumours of AMD's MI400 racks being delayed surface, though credibility remains low](https://x.com/Alex_Intel_/status/2023453704289198429)
* [Rumours of NVIDIA's VR200 racks being ahead of schedule - something that seemed impossible just weeks ago](https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-denies-report-of-mi455x-delays-as-nvidia-vr200-systems-are-rumored-to-arrive-early-company-says-helios-systems-on-target-for-2h-2026)
* [China's GPU manufacturers race to power Chinese frontier models, domestic market now contested by NVIDIA again](https://www.digitimes.com/news/a20260216VL208/gpu-moore-threads-chips-performance-demand.html)
* [Rubin CPX might end up using HBM after all instead of GDDR7](https://x.com/jukan05/status/2025728266473213974)

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)
