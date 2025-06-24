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

Many AI datacentres outside of hyperscalers and the largest of neoclouds are still getting accustomed to the cable densities and optical transceiver failure rates of 51.2T switches. Despite this, Broadcom progresses and announces a 102.4T switch ASIC: the Tomahawk 6.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/tomahawk6_chip.png)

*Source: Broadcom*

Typically, supporting such high bandwidths on a single platform requires multiple distinct ASICs  

512 lanes of 200G, can be used as 1024 lanes of 100G - This means it can connect 1000 devices on a single switch with a pretty reasonable performance. 

Two tier fabrics with this can now server extremely large clusters. How exactly 100,000K devices can be connected is not given but assuming its a classic two tier design

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/june/images/tomahawk6_topology.jpg)

*Source: Broadcom*

can provide 128 ports of 800G or 64 ports of 1.6T - a single asic, arguably easier to cool too. 

True 102.4T switches, instead of joint ASIC switches where some connectivity comes at the cost of ASIC bandwidth. 

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
