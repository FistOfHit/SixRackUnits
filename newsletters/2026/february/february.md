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

HBM, arguably the key enabling technology behind production-scale LLMs, appears to be reaching its physical limits. Despite experts forecasting continuous improvement up to 2038, other teams have began working on a new approach that promises progress even sooner.

![ZAM architecture](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_architecture.png)

*Source: TrendForce*

Z-Angle Memory, or ZAM, is a next-generation DRAM-based memory technology designed to compete with HBM in future hardware that will require large volumes of on-device, high-bandwidth memory. Basically, GPUs, TPUs, and whatever other PUs will aim for AI training and bandwidth-intensive inference workloads.

HBM achieves its high-bandwidths by supplying the logic die at the bottom of the stack with signals from all the DRAM dies above it simultaneously, keeping the very wide data bus saturated. This is implemented by using thousands of TSVs (Through-Silicon Vias), each made from a thin layer of copper, that route both power and signal traffic between the dies.

![HBM TSVs](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_hbm.jpeg)

*Source: Block and Files*

Stacking HBM higher and pushing the bandwidths further has worked great so far, with the latest generations (HBM4) reaching 3.3 TB/s per stack, or as much as 50 sticks of DDR5. But as HBM keeps scaling hitting 16 or even 20 layers per stack, the dies in the middle become thermal dead zones where heat generated must pass through multiple low-conductivity layers, creating thermal gradients and hot spots. ZAM addresses exactly this challenge the most.

Here, multiple TSVs are replaced with a single, more central channel for both power and signal routing. A copper contact ring around the edges of each DRAM die connects to the central channel on the die below at a "Z-angle", or diagonally through and across the dies. This creates a more centralised heat distribution and signal routing architecture. As a side-effect, having a single channel instead of many TSVs also means a significant amount of die area (previously lost to empty holes) is now available for more memory capacity.

![ZAM design](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_design.jpg)

*Source: TrendForce*

Sources state that this new architecture could allow for up to 50% reduction in power consumption compared to HBM (assuming similar performance), and a significant increase in memory capacity per module, as much as 512GB, though no official confirmation or further details on this have been provided yet.

As for the motivation behind all this, it appears to be more than just chasing performance and reliability. This new technology is being developed as part of the NGDB (Next Generation DRAM Bonding) initiative, a collaboration between Intel (U.S. DOE's Advanced Memory Technology program) and SoftBank (SAIMEMORY), with research from the University of Tokyo. This means a high-bandwidth memory technology (and research) independent of SK-Hynix and Samsung, both Korean tech giants.

The geopolitical effects and de-monopolisation efforts of such key technologies have been powerful driving forces in steering AI development in recent times. Which hardware designers get access to a reliable supply of HBM, at whatever cost, will determine their survival and the survival of all of their customers - hyperscalers, AI foundation labs, and everyone in between. It makes sense then that non-Korean teams will continue to push for HBM alternatives as soon as possible.

![HBM roadmap](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_hbm_roadmap.png)

*Source: KAIST teralabs*

We can expect to see ZAM samples entering the market in 2028, with mass production expected in 2029, competing with HBM4E and HBM5 according to current timelines.


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
