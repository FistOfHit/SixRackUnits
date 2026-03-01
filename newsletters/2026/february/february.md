[![Header](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# February 2026

![Title](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/title.png)

*History is supposed to repeat itself. Usually, we look back at the past year to how our plans unfolded and developed and try to learn from that, to see what we can do differently this year. This of course, assumes that the coming year will be the same as the year the passed. The same patterns, people, and processes that we've already seen. It looks like this is no longer the case though, at least in our industry. Every year it seems things change faster than we can keep up with. Patterns we saw in markets or technology don't repeat, each development or hurdle seems to be completely new and unpredictable, and in this case, what should one do? To know how to best act in the future, do we still study history, or actively strive to forget it?*

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top of everything, or even summarising all the material available can be difficult - so we do it for you.

For a space to share sources and news/updates, join our [telegram channel](https://t.me/aihpc_infra_fans) or if you like short form posts on similar topics, check out the [notes section](https://sixrackunits.substack.com/notes) of this newsletter or my [LinkedIn](https://www.linkedin.com/in/hitesh-kumar-6ru).

**[This month's updates](#this-months-updates)**

- [**ZAM**](#zam)
- [**HBM news**](#hbm-news)
- [**Other notable headlines**](#other-notable-headlines)

---

# This month's updates

## ZAM

HBM, arguably the key enabling technology behind production-scale LLMs, appears to be reaching its physical limits. Despite experts [forecasting continuous improvement](https://tera.kaist.ac.kr/researches/teralab-hbm-milestone-and-roadmap) up to 2038, other teams have started working on a new approach that promises progress even sooner.

![ZAM architecture](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_architecture.png)

*Source: TrendForce*

Z-Angle Memory, or ZAM, is a next-generation DRAM-based memory technology designed to compete with HBM in future hardware that will require large volumes of on-device, high-bandwidth memory. Basically, GPUs, TPUs, and whatever other PUs will aim for AI training and bandwidth-intensive inference workloads.

HBM achieves its high-bandwidths by supplying the logic die at the bottom of the stack with signals from all the DRAM dies above it simultaneously, keeping the very wide data bus saturated. This is implemented by using thousands of TSVs (Through-Silicon Vias), each made from a thin layer of copper, that route both power and signal traffic between the dies.

![HBM TSVs](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_hbm.jpeg)

*Source: Block and Files*

Stacking HBM higher and pushing the bandwidths further has worked great so far, with the latest generations (HBM4) [reaching a maximum of 3.3 TB/s per stack](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing), or as much as 50 sticks of DDR5. But as HBM keeps scaling hitting 16 or even 20 layers per stack, the dies in the middle become thermal dead zones where heat generated must pass through multiple low-conductivity layers, creating thermal gradients and hot spots. ZAM addresses exactly this challenge the most.

Here, multiple TSVs are replaced with a [single, more central channel](https://www.linkedin.com/pulse/zam-architectural-alternative-hbm-sharada-yeluri-p8rmc/) for both power and signal routing. A copper contact ring around the edges of each DRAM die connects to the central channel on the die below at a "Z-angle", or diagonally through and across the dies. This creates a more centralised heat distribution and signal routing architecture. As a side-effect, having a single channel instead of many TSVs also means a significant amount of die area (previously lost to empty holes) is now available for more memory capacity.

![ZAM design](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_design.jpg)

*Source: TrendForce*

[Sources state](https://wccftech.com/intel-showcases-its-zam-memory-prototype-for-the-first-time/) that this new architecture could allow for up to 50% reduction in power consumption compared to HBM (assuming similar performance), and a significant increase in memory capacity per module, as much as 512GB, though no official confirmation or further details on this have been provided yet.

As for the motivation behind all this, it appears to be more than just chasing performance and reliability. This new technology is being developed as part of the [NGDB (Next Generation DRAM Bonding)](https://www.softbank.jp/en/corp/news/press/sbkk/2026/20260203_01/) initiative, a collaboration between Intel (U.S. DOE's Advanced Memory Technology program) and SoftBank (SAIMEMORY), with research from the University of Tokyo. This means a high-bandwidth memory technology (and research) [independent of SK-Hynix and Samsung](https://tspasemiconductor.substack.com/p/can-zam-replace-hbm-intel-and-softbank), both Korean tech giants.

The geopolitical effects and de-monopolisation efforts of such key technologies have been powerful driving forces in steering AI development in recent times. Which hardware designers get access to a reliable supply of HBM, at whatever cost, will determine their survival and the survival of all of their customers - hyperscalers, AI foundation labs, and everyone in between. It makes sense then that non-Korean teams will continue to push for HBM alternatives as soon as possible.

![HBM roadmap](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2026/february/images/zam_hbm_roadmap.png)

*Source: KAIST teralabs*

We can expect to see ZAM samples entering the market in 2028, with mass production expected in 2029, competing with HBM4E and HBM5 according to current timelines.

## Memory news

Memory news comes in it's own section this month (and maybe for the rest of time) as there's just so much going on. Below we'll look at developments from the major memory manufacturers, and the plans their customers are making around the memory shortages caused by such insatiable demand.

### NVIDIA

NVIDIA's roadmap is now being shaped by the availability of memory, despite SK-Hynix and Samsung's best efforts to pander to every one of Jensen's requests. [Korean sources](https://m.etnews.com/20260219000091) state that NVIDIA is considering a dual-bin strategy for its upcoming Rubin product line, optimising against the performance vs stability curve, and quite likely also for supply volume. This means that the "top bin" HBM modules which can reliably sustain 11.7Gbps/pin will be used for the higher end SKUs like the Rubin "R200" GPUs, whilst the "bottom bin" ~10Gbps modules will be used for the lower end SKUs like the Rubin SXM GPUs used in HGX servers or even any yet-to-be-announced Rubin series PCIe cards (I have it on good word there will be at-least one in mass production 4Q26).

### HBF

SanDisk announced their intent to create high-bandwidth flash (HBF) just over a year ago now, but so far haven't developed any physical samples or even lab prototypes. That might change very soon though as they've announced a collaboration with SK-Hynix to create standards for the technology and eventually bring it to market.

So far, [SK-Hynix have demonstrated](https://www.trendforce.com/news/2026/01/16/news-expert-says-hbf-may-be-deployed-in-nvidia-gpus-by-2027-28-market-could-surpass-hbm-by-2038/) that HBF shows promise at-least in the simulation space, with their new technology dubbed "H3", which brings together HBM and HBF modules on a single device. Pairing a (simulated) B200 GPU with 8 (simulated) each of HBM and HBF modules, they demonstrated up to 2.69x improvements in performance per watt in (simulated) AI inferencing workloads. Whilst this is far from a serious signal, it indicates that research is going well and sampling is coming soon. Even more recently, five days ago on the 25th of February, the two held a kick-off event at the SanDisk global headquarters and formally launched a joint project under the Open Compute Project (OCP).

Some sources claim that these new HBF modules could reach as high as 512 GB in capacity, and sustaining just over 1.6TB/s of bandwidth, making it perfect for a new tier of on-device memory helping further reduce the need for high-speed interconnects and distant, much slower host memory.

[Un-named industry sources](https://www.sisajournal-e.com/news/articleView.html?idxno=418621) state that HBF could enter commercialisation (mass production) as early as late 2027 for the very early adopters, and would be deployed widely by 2028-2030, putting it alongside HBM6 in future AI accelerators.

### Samsung

Samsung always finds themselves in the middle of a lot of stories, but for now we'll discuss just two: their fast HBM4 for NVIDIA, and their push towards LPDDR6X for Qualcomm.

As we stated earlier, NVIDIA was just recently driving the development of HBM4, with [demands for higher pin rates](https://www.tweaktown.com/news/107669/nvidia-asked-for-9gbps-on-hbm4-then-for-10-11gbps-samsungs-hbm4-looks-superior-for-10gbps-plus/index.html) and greater supply volumes. The market reacted promptly with both SK-Hynix and Samsung pushing the pin rates from the JEDEC standardised 8 Gbps up to 10 Gbps, and then even as high as 11.7 Gbps in their efforts to compete for NVIDIAs orders. Though now with physical constraints being realised, it appears that memory availability is now [driving AI accelerator release timelines](https://x.com/jukan05/status/2021158546692505975) and [manufacturing decisions](https://m.etnews.com/20260219000091).

Through all of this, [Samsung has announced](https://www.tweaktown.com/news/110147/samsung-officially-ships-hbm4-ready-for-nvidias-next-gen-rubin-ai-chips/index.html?utm_source=newsletter) that their HBM4 modules are "commercially shipping" which likely just means that they've entered mass production and delivery. We also now learn that these modules can be overclocked to reach past even 11.7 Gbps, all the way to 13 Gbps per pin. For a HBM4 module with 2048 pins, that's 3.3 TB/s out of a capacity of 24 or 32 GB.

Moving onto LPDDR6X, Samsung has [reportedly began shipping](https://www.tweaktown.com/news/110149/sk-hynix-shows-off-16gb-lpddr6-at-14-4gbps-while-samsung-sends-lpddr6x-samples-to-qualcomm/index.html) samples to Qualcomm for use in their upcoming AI200 and AI250 AI accelerators.

Qualcomm have been working on their own AI inferencing accelerators for close to 7 years now, with the original "Cloud AI 100" announed back in April of 2019. Since then, Qualcomm have sold a reasonable number of units (iterations upon the Cloud AI 100 that is) to various clouds such as AWS and Cirrascale to name the biggest, and have worked their way into GigaByte (of course), HPE, Lenovo, and even Dell's datacentre servers offerings.

Now for the latest in this product line, the AI200 and AI250s, Qualcomm will likely be sourcing highly energy-efficient and fast LPDDR6X from Samsung. The capacity and pin rates aren't yet revealed, but likely they'll be in 2GB or 4GB volumes, and pushing anywhere from 12.8 Gbps (Samsung's current gen. LPDDR6 performance) up to well beyond 14.4 Gbps per pin. [SK-Hynix's LPDDR6](https://www.tweaktown.com/news/110149/sk-hynix-shows-off-16gb-lpddr6-at-14-4gbps-while-samsung-sends-lpddr6x-samples-to-qualcomm/index.html) is already overclocking at 14.4 Gbps and so naturally the higher end of the X-generation will have to have a theoretical limit higher than that.

Originally targeting smartphones or other low-power devices in need of faster memory, LPDDR is now popular for AI accelerators optimising for performance per watt such as Qualcomm's AI200/250s, IBM's Spyre, NVIDIA's Grace/Vera CPUs, and more.

### Micron

[Micron finally enters the GDDR7 game](https://www.tomshardware.com/pc-components/gpus/micron-joins-the-3gb-gddr7-party-introduces-36-gbps-modules-for-gpus-lags-behind-speeds-of-samsung-and-sk-hynix) with their 3GB modules, despite each reaching only 36GB/s in bandwidth. Compared to their Korean competition in SK-Hynix and Samsung [(both promising 40GB/s+)](https://wccftech.com/sk-hynix-gddr7-memory-boosts-gpu-bandwidth-160-gb-s-40-gbps-24-capacity/), Micron's Graphics DDR appears to be a less attractive product at first. This is almost certainly the case for buyers placing them in AI accelerators, which run at high wattages and with active cooling methods usually. But for anyone buying GDDR for graphics accelerators like NVIDIA's RTX or AMD's Radeon cards, memory modules are often chosen to be of a lower specification or even down-clocked to fit into more modest power and thermal profiles.

Too bad that there are currently serious gaming GPU shortages plaguing the market right now. Even worse, NVIDIA just announced that there will be [no new graphics cards](https://www.xda-developers.com/this-is-the-first-year-in-three-decades-without-a-new-nvidia-gaming-gpu/) released this year, making it a pretty sad year for gamers and lower-end GDDR manufacturers alike. Regardless, Micron will probably still sell their GDDR7 inventory completely for use in PCIe form-factor AI accelerators like the RTX Pro 6000/D or prefill-focused GPUs like the Rubin CPX.

---

## Other notable headlines

* [InferenceMAX v2 (now called InferenceX) is out - SemiAnalysis](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)
* [NVIDIA pushes Samsung to deliver HBM4 even faster](https://www.chosun.com/economy/tech_it/2026/02/04/I2W4VIHCG5C4XL4Z2EF3X72WDE/)
* [China's HBM3 production is narrowing the gap with the South Korean giants](https://www.mk.co.kr/news/business/11957166)
* [Nvidia's new RTX 6000D appears in teardown: 84GB GDDR7 in China compared to the full 96GB](https://www.tweaktown.com/news/110135/nvidias-new-rtx-6000d-appears-in-teardown-84gb-gddr7-in-china-compared-to-the-full-96gb/index.html)
* [World's first PCIe 6.0 SSD enters mass production with 28GB/s speeds: Micron 9650 series SSDs support air and liquid cooling](https://www.tomshardware.com/pc-components/ssds/worlds-first-pcie-6-0-ssd-enters-mass-production-with-28gb-s-speeds-micron-9650-series-ssds-support-air-and-liquid-cooling)
* [Cisco releases the G300 102.4T switch ASIC](https://mp.weixin.qq.com/s?chksm=e8bf1883dfc89195350bb6dec790d823de6074dac8e9042aa966f21dfca7c113e384fce3d3cb&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1770883821_3&req_id=1770883878521405&mid=2247488461&sn=975a51dd4d8b1c5900c6b59d8ceb81db&idx=1&__biz=MzIyOTcyNzc3Nw%3D%3D&scene=169&subscene=200&sessionid=1770883820)
* [Evercore out with a 4Q25 AI Channel Checks, saying $NVDA Vera Rubin appears to be ahead of schedule (Tweet by @halfblindmonkey)](https://x.com/halfblindmonkey/status/2023737861028098525)
* [Rumours of AMD's MI400 racks being delayed surface, though credibility remains low](https://x.com/Alex_Intel_/status/2023453704289198429)
* [Rumours of NVIDIA's VR200 racks being ahead of schedule...](https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-denies-report-of-mi455x-delays-as-nvidia-vr200-systems-are-rumored-to-arrive-early-company-says-helios-systems-on-target-for-2h-2026)[But also rumours that they'll be delayed](https://x.com/jukan05/status/2026228673775562820)
* [China's GPU manufacturers race to power Chinese frontier models, domestic market now contested by NVIDIA again](https://www.digitimes.com/news/a20260216VL208/gpu-moore-threads-chips-performance-demand.html)
* [Rubin CPX might end up using HBM after all instead of GDDR7](https://x.com/jukan05/status/2025728266473213974)
* [Sambanova introduces new AI accelerator SN50, claims to be three times more efficient than Nvidia B200](https://www.tomshardware.com/tech-industry/artificial-intelligence/sambanova-introduces-new-ai-accelerator-partners-with-intel-to-deploy-xeon-cpus-for-inferencing-and-agentic-workloads-sambanova-claims-sn50-chip-is-three-times-more-efficient-than-nvidia-b200)
* [Nvidia delivers first Vera Rubin AI GPU samples to customers](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-delivers-first-vera-rubin-ai-gpu-samples-to-customers-88-core-vera-cpu-paired-with-rubin-gpus-with-288-gb-of-hbm4-memory-apiece)
* [Bytedance developing internal AI ASIC, in manufacturing talks with Samsung](https://www.reuters.com/world/asia-pacific/bytedance-developing-ai-chip-manufacturing-talks-with-samsung-sources-say-2026-02-11/)

---

[![Footer](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)
