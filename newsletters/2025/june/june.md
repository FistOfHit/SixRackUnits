[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# June 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/title.jpg)

*If it turns out that biological-based computing is indeed the most efficient way to process data, then what will supercomputers - and hence datacentres - look like?*

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top and even summarising all the material available can be difficult - so we do it for you!

For a space to share sources and news/updates, check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a> for posts on similar topics!

[**This month's updates:**](#this-months-updates)
  - [**AMD delivers a roadmap to defeat Nvidia**](#amd-delivers-a-roadmap-to-defeat-nvidia)
  - [**Broadcom shows the world a 100 Terabit switch ASIC: Tomahawk 6**](#broadcom-shows-the-world-a-100-terabit-switch-asic-tomahawk-6)
  - [**1 PB/s planned for HBM within the next decade, KAIST reveals**](#1-pb-s-planned-for-hbm-within-the-next-decade-kaist-reveals)
  - [**OmniPath might still make a comeback: Cornelis announces the CN5000 spec**](#omnipath-might-still-make-a-comeback-cornelis-announces-the-cn5000-spec)
  - [**Other notable headlines**](#other-notable-headlines)

---

# This month's updates:

## AMD delivers a roadmap to defeat Nvidia

At their Advancing AI 2025 event this month, AMD delivered a reveal rivalling Nvidia's GTC last quarter. In it, AMD showed commitment to taking on the datacenter GPU market with a solid roadmap, heading towards the most performant GPUs and the most ambitious rack-scale products in the industry.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_rack_roadmap.jpg)

*Source: AMD*

The roadmap charts a path through the three key routes towards dominance in AI training: CPUs, GPUs, and NICs. The Imminent "rack-scale" solution (2H25) is a not a particularly interesting stepping stone as it will still use a scale-out fabric between servers on the same rack, so as a quick summary: 64 MI350X air-cooled or 96/128 MI355X liquid-cooled GPUs, 5th gen. Turin CPUs, and Pollara 400G UEC (Ultra Ethernet Consortium) compatible NICs.

This product might still be quite popular among some hyperscalers wishing to deploy in volume, with OCI (Oracle Cloud Infrastructure) saying that they are preparing [to deploy 130K](https://www.datacenterdynamics.com/en/news/oracle-to-deploy-cluster-of-more-than-130000-amd-mi355x-gpus/) (131,072) MI355X GPUs. This is unsurprising given that they have a very mature datacentre operations business and so won't be as impacted by the 40% increase in GPU TDP (see below for specs) as much as neoclouds or smaller datacentre build-outs would.

Given that there will be [no APU form](https://www.techradar.com/pro/amd-unveils-puzzling-new-mi355x-ai-gpu-as-it-acknowledges-there-wont-be-any-ai-apu-for-now) of the 350 series, it's entirely possible that the 355X was developed purely for Oracle and other hyperscalers who committed enough to justify a rather odd SKU like this.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_title.jpg)

*Source: AMD*

The much more interesting part of the future begins in 2H26 with what AMD call the "Helios" architecture. According to [SemiAnalysis' estimates](https://semianalysis.com/2025/06/13/amd-advancing-ai-mi350x-and-mi400-ualoe72-mi500-ual256/#introducing-the-mi400-helios-rack), this will be a double-width rack supporting:

- 72 MI400X or MI450X GPUs
- 18 7th Gen. "Venice" CPUs
- 216 "Vulcano" 800G NICs
- 6 scale-up trays @ 204.8T each
- 6 scale-out trays @ 51.2T each

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_rack_diagram.png)

*Source: SemiAnalysis - The title which names the MI450X instead of the MI400X appears to be a typo, though it's not hard to imagine that the 400 series will have an intermediate refresh before the 500 releases. In fact, the 450 might be the rack-scale version of the 400, designed for DLC in very dense setups.*

Below is SemiAnalysis' (estimated) diagram of the compute tray architecture:

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_block_diagram2.png)

*Source: SemiAnalysis*

This implies the following specs:

- 720 PFLOPs at FP16
- 31.1 TB/s of HBM4 @ 1.4 PB/s aggregate bandwidth
- ~130 TB/s all-all scale-up bandwidth
- ~173 Tb/s (bits, not bytes) uni-directional aggregate scale-out bandwidth

These values are designed to match/surpass not Nvidia's Blackwell Ultra (GB300), but the Rubin's (VR200) expected performance. In terms of scale-up domain, AMD is targeting [NVLink gen. 5](https://www.nvidia.com/en-gb/data-center/nvlink/) (1.8TB/s), and for the scale-out they're pushing past at 2.4Tbps/GPU, 1.5x that of NVidia's plans built around its [upcoming CX-9 NICs](https://www.datacenterdynamics.com/en/news/nvidia-announces-vera-rubin-superchip-for-late-2026/).

The options available for the topologies here are quite interesting. If we assume the SemiAnalysis estimates for the Helios's architecture, then the scale-up will be powered by 12 x 102.4T ASCIs ([Broadcom's Tomahawk 6](https://www.broadcom.com/company/news/product-releases/63146) is the only one available currently) which will present as 512 x 200Gbps ports each, for a total of 6144 x 200Gbps or 85.3 x 1.8TB/s connections. This means that each of the 12 ASICs can take 432 links, 6 from each of the 72 GPUs, and each GPU in turn exposes 72 links to the network. One possible topology is shown below:

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_scale_up_topology.png)

*Source: SixRackUnits - I made this independently of the SemiAnalysis diagram, I promise! Honestly forgot that existed.*

Similarly for the scale-out, one possible simple topology is given below:

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_scale_out_topology.png)

*Source: SixRackUnits - I doubt this is the best possible setup, but it's the simplest one that I could think of.*

In both cases, we assume that the Vulcano 800G NICs would present dual 400G ports each, which would have the primary benefit of allowing for a wider range of OSFP or QSFP/QSFP-DD optics rather than 800G OSFP or other niche form factors albeit at the cost of additional parts and perhaps more energy consumption. In the case that NICs adopt CPO (Co-Packaged Optics) technology (though there isn't any information on this), then optics wouldn't be a factor but multiple ports would still be better in terms of redundancy and perhaps even performance.

*Speculation:*
It's possible, but not supported by any sources yet, that AMD could move towards a dual (or even triple) plane architecture such as [Alibaba's HPN](https://ennanzhai.github.io/pub/sigcomm24-hpn.pdf). In this design, two identical versions of a 400G network connect to the same endpoints providing additional paths and hence more options for the network management algorithms to keep performance high under heavy, chaotic traffic patterns. In this case, it could mean that that each scale-out switch contains two 25.6T switch ASICs for physical separation of the planes, or that only three or two of the 6 switches are used per plane. Diagrams not provided.

Finally, some stats for all the new reveals, including both confirmed and estimated values ([1](https://www.tomshardware.com/pc-components/gpus/amd-announces-mi350x-and-mi355x-ai-gpus-claims-up-to-4x-generational-gain-up-to-35x-faster-inference-performance) [2](https://www.kedglobal.com/korean-chipmakers/newsView/ked202506130004) [3](https://morethanmoore.substack.com/p/amds-ai-future-is-rack-scale-helios) [4](https://www.amd.com/en/blogs/2025/amd-instinct-mi350-series-and-beyond-accelerating-the-future-of-ai-and-hpc.html) [5](https://www.amd.com/en/blogs/2025/amd-delivering-open-rack-scale-ai-infrastructure-to-unlock-agentic-ai.html) [6](https://x.com/Jukanlosreve/status/1933729517937569954)):

### MI350X:

- 288GB HBM3E 12Hi @ 8TB/s: 8 stacks of 36GB each (Samsung + Micron)
- ~4.6/9.3/18.5 PFLOPs @ FP16/8/4, ~72/144 TFLOPs @ FP64/32
- 1000W TBP (Total Board Power)
- Using TSMCs "N3P" 3nm and "N6" 6nm processes
- Shipping 2H25
- 256MB AMD "Ininifity Cache" (sort of similar to L3 cache)
- PCIe 5.0 x16 H2D interconnect
- 1/2.2 GHz Base/Boost clock
- Focusing on air-cooled deployments

### MI355X:

- 288GB HBM3E 12Hi @ 8TB/s: 8 stacks of 36GB each (Samsung + Micron)
- ~5.0/10.1/20.1 PFLOPs @ FP16/8/4, ~79/158 TFLOPs @ FP64
- 1400W TBP (Total Board Power)
- Using TSMCs "N3P" 3nm and "N6" 6nm processes
- Shipping 2H25
- 256MB AMD "Ininifity Cache" (sort of similar to L3 cache)*
- PCIe 5.0 x16 H2D interconnect*
- 1/2.4 GHz Base/Boost clock
- Focusing on liquid cooled deployments

### MI400X:

- 432GB HBM4 @ 19.6TB/s:
- ~10/20/40 PFLOPs @ FP16/8/4
- 2300W TDP
- 1.8TB/s scale-up bandwidth
- 2400Gb/s scale out bandwidth (3 x 800G NICs per GPU)

### MI450X:

- Nothing new of significance found yet

### MI500X:

- Reportedly either TSMCs "N2P" 2nm process or some 14A process**

*Assuming that the 355 will be very similar to the 350 in terms of architecture and composition.
**The [source](https://www-nextplatform-com.cdn.ampproject.org/c/s/www.nextplatform.com/2025/06/12/amd-plots-interception-course-with-nvidia-gpu-and-system-roadmaps/amp/) that claims that the MI500X will use a 14A process node does not provide any justification for this statement.

[SemiAnalysis](https://semianalysis.com/2025/06/13/amd-advancing-ai-mi350x-and-mi400-ualoe72-mi500-ual256/#introducing-the-mi400-helios-rack) and other sources mentioned above go much further into the details of the announcements, they are all well worth a read.

---

## Broadcom shows the world a 100 Terabit switch ASIC: Tomahawk 6

51.2T switches - network switches that support up to 51.2 Tbps of aggregate bandwidth - are still only seen in large-scale high-end AI datacentres. [Usually implemented](https://www.arista.com/assets/data/pdf/Datasheets/7060X6-Datasheet.pdf) as a 2U chassis of 64 x 800G ports, these switches power modern non-blocking east-west or backend fabrics. With the cable densities and transceiver counts used in large scale deployments such as Nvidia SuperPods, many datacentres have had a [difficult time](https://cxotechmagazine.com/cable-plant-matters-in-the-rapidly-changing-data-center-landscape/) adapting to such high-bandwidth networking infrastructure.

Despite all of this, Broadcom targets the prepared and eager datacentres of the near future by announcing a 102.4T switch ASIC: the [Tomahawk 6](https://www.broadcom.com/products/ethernet-connectivity/switching/strataxgs/bcm78910-series). The chip will come in [512 x 200G lane and 1024 x 100G lane SKUs](https://www.naddod.com/blog/broadcom-tomahawk-6-102-4-t-ethernet-switch-chip-for-ai-fabrics), with the latter being significantly larger due to the increased shoreline (perimeter) required to support that many physical lanes. In addition, a [CPO (Co-Packaged Optics) version](https://www.gazettabyte.com/home/2025/6/3/tomahawk-6-the-industrys-first-100-terabit-switch-chip.html#:~:text=Co%2Dpackaged%20optics:%20Enhancing%20reliability?) of the chip will be available, for near-future switch platforms competing with Nvidia's upcoming QuantumX-800 and SpectrumX products. 

Note that this is not a 102.4T switch, which may consist of multiple ASICs (chips), but a single chip.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/tomahawk6_chip.png)

*Source: Broadcom*

Among the many claims made by Broadcom regarding the ASIC's performance, the most interesting was its ability to support 100,000+ "XPUs", or devices, on a two-tier network. Typically, for a non-blocking spine-leaf network topology as is common in [Nvidia's SuperPod reference architectures](https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-h100/latest/dgx-superpod-architecture.html), three tiers of switches are required when scaling to large numbers of devices. This is because in switches like Nvidia's SN5600 and Arista's 7060DX5-64S provide 64 ports of 400G each, which means that a single switch can connect to 32 devices at 400G (the other 32 ports are needed for uplink to the spine layer). With this domain size for a single switch, 64 such switches can be used in the leaf layer, with each spine switch having 64 ports to connect to each leaf switch. This then implies a maximum of 64 x 32 = 2048 devices in a two tier topology, using these switches, at a 400G bandwidth. 

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/tomahawk6_topology.jpg)

*Source: Broadcom*

The Tomahawk 6, on the other hand, is promised by Broadcom to support 131,072 devices at 200G. One possible topology is shown below, a non-blocking spine-leaf setup (not-rail optimised because the diagram would get too complicated). To increase the bandwidth of the fabric without introducing a third tier, [multiple "planes"](https://www.gazettabyte.com/home/2025/6/3/tomahawk-6-the-industrys-first-100-terabit-switch-chip.html#:~:text=Wide%20and%20flat%20topologies), or parallel implementations of this topology, can be used with extensive breakout in the ports/cabling. The benefit of such a setup would be the simplicity retained by each two-tier plane when it comes to congestion control, resulting in a more efficient and performant fabric overall.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/tomahawk6_100k.png)

*Source: SixRackUnits*

The customers for the ASIC haven't been made public yet, but it's confirmed that sampling is underway, with mass production and hence integration into switches expected to start in 2Q26.

---

## 1 PB/s planned for HBM within the next decade, KAIST reveals

The three major memory makers - SK Hynix, Samsung, and Micron -  are all working on their own implementations of HBM4, hoping to secure orders from the likes of Nvidia and AMD for their upcoming GPUs. The balance is tipping it seems with SK-hynix [already sampling HBM4](https://dealsite.co.kr/articles/143019) and possibly even discussing [custom HBM4](https://www.kedglobal.com/korean-chipmakers/newsView/ked202506190003) implementations with some customers, whilst Samsung is [still struggling](https://www.linkedin.com/pulse/sk-hynix-micron-hbm4-qualification-nvidia-done-deal-samsung-baratte-jp5yf/) to pass Nvidia's qualification for HBM3E, but there is still a lot of potential for change.

Meanwhile, the KAIST (Korea Advanced Institute of Science and Technology) Teralab research group recently [presented a roadmap](https://drive.google.com/file/d/1wdGvyAYM0SOjlweJcgPDKwXlk6czbuZo/view?pli=1) detailing the current trends and future plans for HBM. Extending out to 2038, the roadmap reaches HBM8 and speculates that packages (devices essentially) will reach ~1PB/s of aggregate memory bandwidth from 6TB worth of HBM modules, as well as requiring up to 15kW of power and futuristic "embedded-in-chip" liquid cooling methods.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/HBM_roadmap2.jpg)

*Source: KAIST TERA*

Teralab have an extensive history of research on semiconductor packaging, interconnects, and HBM in particular, and have also [collaborated](https://tera.kaist.ac.kr/projects/industry-collaboration-partners) with both SK Hynix and Samsung on HBM and surrounding technologies. The 371-slide presentation was part of a significant effort to understand the current technological and economic trends shown in the memory markets in addition to well-informed speculation based on current and planned research. The full slides are available [here](https://drive.google.com/file/d/1wdGvyAYM0SOjlweJcgPDKwXlk6czbuZo/view?pli=1).

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/HBM_roadmap.png)

*Source: KAIST TERA*

According to forecasts by the group, data rates for pins that connect the HBM module interface to the compute dies will level off at about double that of current HBM3E implementations. The capacity of individual memory dies however, should increase by ~3.5x, driven by denser process nodes and large die sizes. The leading hope for these incredible predictions though is the total module bandwidth increase, expected to jump sharply over the next decade due to stack height and bus width increases. 

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/HBM_forecast.png)

*Source: KAIST TERA*

Based on how the increased stack heights, die densities, and module power usage all compound to increase heat generation, current cooling methods will not be able to keep up. Teralab propose two new methods: dedicated module immersion tanks and in-chip embedded liquid cooling.

The former is implemented already at a more macro-level, where entire servers can be dipped into tanks of non-conductive fluids, but is still constrained to research lab supercomputers ([1](https://esg.tsmc.com/en/update/innovationAndService/caseStudy/42/index.html) [2](https://www.amd.com/en/resources/case-studies/shell.html)) rather than hyperscaler datacentres. The proposed method here however shrinks the domain of immersion to the chip/stacks themselves, isolating the fluid and allowing for a dedicated supply to each module.

The latter is seemingly a much more complex and involved method requiring integrating the cooling system into the chip manufacturing process too, but appears to show promise for significantly greater cooling capabilities than the current state-of-the-art. Presently, implementations of all such cooling systems remain in the research domain ([1](https://www.eenewseurope.com/en/steam-cooling-embedded-in-hot-chips/) [2](https://www.iis.u-tokyo.ac.jp/en/news/4747/) [3](https://www.mdpi.com/2072-666X/13/6/918)).

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/HBM_cooling.png)

*Source: KAIST TERA*

The presentation goes further into specifics on current and future research streams, and also talks about future SoC (System-on-Chip) designs created around HBM stacks rather than compute chips. Detail is given on how other memory technologies such as LPDDR die and [HBF (High Bandwidth Flash)](https://www.tomshardware.com/pc-components/dram/sandisks-new-hbf-memory-enables-up-to-4tb-of-vram-on-gpus-matches-hbm-bandwidth-at-higher-capacity) can be integrated onto future packages, controlled by HBM logic die to provide CPU-independent tiered memory systems for compute. For more on this, see the slides [here](https://drive.google.com/file/d/1wdGvyAYM0SOjlweJcgPDKwXlk6czbuZo/view?pli=1).

---

## OmniPath might still make a comeback: Cornelis announces the CN5000 spec

The modern networking market for AI is often seen as a two-horse race between InfiniBand and Ethernet, the first being an established standard for HPC and AI applications, and the second being the underdog who is rapidly catching up at smaller and medium scales and usually was the only real solution at extremely large scales. There are other players each bringing their own pros and cons, but most only really being useful in very specific situations.

OmniPath, now advanced by [Cornelis networks](https://www.cornelisnetworks.com/) (but [developed originally](https://en.wikipedia.org/wiki/Omni-Path) by Intel), is another competitor which appears to meet the criteria for being a viable datacentre data fabric: scalability, performance, and availability.

Introducing speeds of up to 400Gbps for a lossless and congestion-free fabric, as well as message injection rates "2x greater than InfiniBand NDR", OmniPath is sticking to its USP of having better latency than other fabrics. Though now, rather than staying in the shadows with research labs running HPC applications, Cornelis wants to bring OmniPath into the limelight [with AI](https://www.cornelisnetworks.com/pdf-archive/2023/11/CN5000_Family_Product_Brief_A00337.pdf).

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/omnipath_roadmap.jpg)

*Source: Cornelis Networks*

This is essentially the same plan they had in 2024 as well, predicting that UEC (Ultra Ethernet Consortium) compatible hardware would only be available in mass around 2027, despite the standard being finalised just this month. This is a sensible bet given how long it takes consortiums to progress from paperwork to implementation but given the urgency that industry is showing when moving away from InfiniBand, its possible that vendors will release limited ranges of [UEC-ready products in 2H25](https://www.tomshardware.com/networking/amd-deploys-its-first-ultra-ethernet-ready-network-card-pensando-pollara-provides-up-to-400-gbps-performance)

Current plans for the CN5000 technology is to support 400G fabrics for up to 500K endpoints (devices), but by 2027 that should quadruple to 1.6T and 2 million endpoints, showing a good understanding of where the market is heading for hyperscalers, neoclouds, and AI labs. In addition, OmniPath will support Ethernet next year and then UEC the year after next, signalling that Cornelis do not intend to make the same mistakes that Nvidia did until last year with aggressive [vendor lock-in](https://www.fierce-network.com/data-center/hyperscalers-want-replace-infiniband-ethernet-heres-why) through InfiniBand.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/omnipath_nic.png)

*Source: Cornelis Networks*

The CN5000 SuperNIC comes in single or dual port PCIe form factors, using gen 5. (~64GB/s uni-directional). Cornelis state the power draw to be 15 or 19W for the single and dual port versions, and will provide SKUs for air-cooled and liquid-cooled versions. [One source](https://mp.weixin.qq.com/s?chksm=ecb43f98dbc3b68e29b778ff3aae6fd8f7d82d0541fba6ea420cfd830af3834ba55852e73d16&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1751105088_3&mid=2247485130&sn=9a8d7061ca4614a56e61db33d0d82442&idx=1&__biz=MzI5NzQxNDcxNw%3D%3D&scene=169&subscene=200&sessionid=1751105088) claims that the NIC is capable of 800 million packets per second, and provides "<1 microsecond latency for MPI" though there are no other sources to corroborate this.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/omnipath_switch.png)

*Source: Cornelis Networks*

[The switch](https://www.cornelisnetworks.com/pdf-archive/2023/11/CN5000_Family_Product_Brief_A00337.pdf) is a 1U, 48-port chassis, with a TDP of 710W empty, or 1.1kW with 48 7.5W AOC (Active Optical Cables) ports. 48 ports is an odd number, and might be from some combination of having multiple interconnected ASICs inside, keeping the form-factor to 1U, reducing or managing latency by keeping the port count low, or some other optimisations to the ASIC for the incredible message rates OmniPath provides. These switches will also come in air and liquid-cooled SKUs.

It should be remarked that very few vendors are open about the power draws of their switches and NICs publicly like Cornelis is.

---

## Other notable headlines

* [Micron ships samples of its gamma process node-based LDPPR5X, showing significant improvements and a promising future for low power chips](https://investors.micron.com/news-releases/news-release-details/micron-ships-worlds-first-1g-1-gamma-based-lpddr5x-enabling-rich)
* [Chinese-aimed RTX Pro 6000D may well have NVLink after all, analysts suggest](https://x.com/Jukanlosreve/status/1929323825780687148?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1929323825780687148%7Ctwgr%5Ed020165ebbddf11e2ba463624b500fcd5fd8d8fe%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.tweaktown.com%2Fnews%2F105564%2Fnvidias-new-china-specific-b30-ai-gpu-allows-multiple-chips-interconnected-to-act-as-one%2Findex.html)
* [SK-Hynix reveals a DRAM roadmap for the next 30 years](https://news.skhynix.com/sk-hynix-presents-future-dram-technology-roadmap-at-ieee-vlsi-2025/)
* [Qualcomm acquires Alphawave for its interconnects capabilities, confirming it's intent to compete in Datacenter AI accelerators](https://www.qualcomm.com/news/releases/2025/06/qualcomm-to-acquire-alphawave-semi)
* [PCIe 7.0 official specification is live, despite gen. 6 adoption being barely visible in industry](https://www.businesswire.com/news/home/20250611299049/en/PCI-SIG-Releases-PCIe-7.0-Specification-to-Support-the-Bandwidth-Demands-of-Artificial-Intelligence-at-128.0-GTs-Transfer-Rates)
* [Nvidia's Rubin GPU and Vera CPU rumoured to not be delayed at all - samples to be produced by September, mass production by 2Q26](https://www.tweaktown.com/news/105660/nvidias-next-gen-rubin-gpu-vera-cpu-rumors-no-delays-new-chips-are-being-moved-up/index.html)
* [Samsung yet again fails HBM3E certification on Nvidia packages, aiming for a re-run in September](https://m.businesspost.co.kr/BP?command=mobile_view&num=398661)
* [SK-Hynix reportedly already supplying small quantities of HBM4 to Nvidia, Micron less than a quarter behind](https://x.com/Jukanlosreve/status/1934381245791883502)
* [AMD's Zen 6 architecture could lead to 7 GHz boost clock rates on CPUs](https://www.tweaktown.com/news/106021/amds-next-gen-zen-6-chips-could-launch-with-crazy-high-7-0ghz-cpu-clock-speeds/index.html?utm_source=newsletter)
* [Samsung might ship HBM4 12Hi samples in early 3Q25, possibly catching up with other the memory makers](https://x.com/Jukanlosreve/status/1938429838794363266)

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)