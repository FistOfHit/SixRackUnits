[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# June 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/title.jpg)

*If it turns out that biological-based computing is indeed the most efficient way to process data, then what will supercomputers - and hence datacentres - look like?*

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. In addition, we also cover vendors of anything interesting in the space, as well as short "one-pagers" on a random topic that we find interesting (and hope you do too).

For a space to share sources and news/updates, check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a> for posts on similar topics!

[**This month's updates:**](#this-months-updates)
  - [**AMD delivers a roadmap to defeat Nvidia**](#amd-delivers-a-roadmap-to-defeat-nvidia)
  - [**Broadcom shows the world a 100 Terabit switch ASIC: Tomahawk 6**](#broadcom-shows-the-world-a-100-terabit-switch-asic-tomahawk-6)
  - [**Huawei's present and future - mixed reactions from the market**](#huawei-s-present-and-future)
  - [**1 PB/s planned for HBM within the next decade, KAIST reveals**](#1-pb-s-planned-for-hbm-within-the-next-decade-kaist-reveals)
  - [**Meta making merchant silicon? Rumours of MTIA rack-scale in 2027**](#meta-making-merchant-silicon-rumours-of-mtia-rack-scale-in-2027)
  - [**Other notable headlines**](#other-notable-headlines)

**Note**: From this issue onwards, I will return to having 5 updates per issue but will now be scrapping the one-pager and vendor spotlight sections. Apologies. 

---

# This month's updates:

## AMD delivers a roadmap to defeat Nvidia

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_title.jpg)

*Source: AMD*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_rack_roadmap.jpg)

*Source: AMD*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_rack_diagram.png)

*Source: AMD*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_dual_rack_diagram.png)

*Source: AMD*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_block_diagram.png)

*Source: AMD*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/AMD_block_diagram2.png)

*Source: AMD*

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

## Huawei's present and future - mixed reactions from the market

**

---

## 1 PB/s planned for HBM within the next decade, KAIST reveals

HBM continues to advance at a rapid pace, with the major memory makers all not jonly keeping up with JEDEC, but also outpacing it and moving to custom designs. 

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/HBM_roadmap2.jpg)

*Source: KAIST TERA*

KAIST Teralab, (why are they an authority on HBM?) presented the future of HBM for the next 10 years. 

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/HBM_roadmap.png)

*Source: KAIST TERA*

Whilst datarates may stall at physical limits based on current copper trace-based signalling methods, the bandwidth will still increase exponentially due to HBM being stacked higher and higher and buses becoming wider. Moving to 1PB per chip in the future. For reference, thats 1000x the bandwidth of the current HBM3E. 

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/HBM_forecast.png)

*Source: KAIST TERA*

Cooling must also keep up since such high stacks cant dissipate heat fast enough to be passively or actively air cooled anymore. Even direct or immersion cooling wont be enough for far future technologies. Will move to direct-in stack cooling. 

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/HBM_cooling.png)

*Source: KAIST TERA*

Worth watching how the key players in HBM space will plan for this and who will emerge as the leader in this space if any. 

---

## Meta making merchant silicon? Rumours of MTIA rack-scale in 2027

**

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
* []()

---
