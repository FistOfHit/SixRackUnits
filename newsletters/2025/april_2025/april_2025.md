[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# April 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/title.jpeg)

*Will we ever move away from cables? What could high-bandwidth, low-error, and secure wireless communications looks like in the future?*

[**This month's updates:**](#this-months-updates)
  - [**Lightmatter's 3D photonics - computing with light**](#lightmatters-3d-photonics---computing-with-light)
  - [**Tenstorrent announces the Blackhole AI accelerator**](#tenstorrent-announces-the-blackhole-ai-accelerator)
  - [**IBM's z17 mainframe - "for the AI age"**](#ibms-z17-mainframe)
  - [**Ironwood: Google's seventh gen. TPU**](#ironwood-googles-seventh-gen-tpu)
  - [**Other notable headlines**](#other-notable-headlines)

[**Vendor spotlight:**](#vendor-spotlight)
  - [**Kove**](#kove)

[**One-pagers:**](#one-pagers)
  - [**Bandiwdth and latency**](#bandwidth-and-latency)
  - [**Liquid cooling plates**](#liquid-cooling-plates)

For a space to share sources and news/updates, join on <a href="https://t.me/aihpc_infra_fans">Telegram</a>, and check out my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a> for posts on similar topics!

---

# This month's updates:

## Lightmatter's 3D photonics - computing with light

## Tenstorrent announces the Blackhole AI accelerator

## IBM's z17 mainframe

## Ironwood: Google's seventh gen. TPU

## Other notable headlines

* [SK-Hynix possibly mass producing both HBM4 and HBM4E this year](https://www.tweaktown.com/news/104464/sk-hynix-confirms-both-hbm4-and-hbm4e-memory-are-coming-this-year-for-next-gen-ai-gpus/index.html)
* [Chinese firms place up to $16 billion of orders for Nvidia's CHIPS act-dodging AI GPUs](https://www.reuters.com/technology/chinese-firms-place-16-billion-order-new-nvidia-chips-information-reports-2025-04-02/)
* [Samsung reportedly begins developing its 1nm "dream" process, ready for mass production in 2029](https://www.trendforce.com/news/2025/04/10/news-samsung-reportedly-begins-1nm-process-development-targets-2029-mass-production/)
* [Nubis communications and Amphenol to develop signal redrivers to enable 200G/lane SERDES across multiple meters of copper, enabling multi-rack scale-up networks without optics](https://www.businesswire.com/news/home/20250326861856/en/CORRECTING-and-REPLACING-Nubis-Extends-Linear-Paradigm-from-Optics-to-Copper-with-Breakthrough-Nitro-Linear-Redriver-Solution-Enabling-4-Meter-Reach-for-200Gbps-per-Lane-Copper-Cables-in-AI-Scale-Up-Networks)
* [UALink (Ultra Accelerator Link) consortium announces their 1.0 specification, at 200G per lane. Aims to provide an open standard against Nvidia's NVLink](https://ualinkconsortium.org/)
---

# Vendor spotlight:

## Kove

*Host memory capacity is and has always been the be-all and end-all of large, high-performance workloads, as triggering an OOM error usually causes not just the application and its progress/state to crash, but the entire host. [Kove](https://kove.com/) are a firm working to change this with a solution for remote, software-defined memory (SDM) that appraoches the performance of local memory.*

Founded in 2003, American firm Kove has quietly been supplying remote memory solutions to customers who found their workloads constrained not by compute, but by memory capacity. Kove's memory tower system presents as a [rack](https://kove.com/products/kovesdm-memory-tower/) of DRAM enclosures containing some management compute and [high-performance NICs](https://arstechnica.com/sponsored/kove-tackles-the-last-software-defined-technology-memory/), and their [software stack](https://kove.com/products/kovesdm-software/) manages the remote memory and transfers to expose a memory pool that can be defined (configured or managed) entirely by software. With a maximum capacity of up to 256TiB (tebibyte, or 2^40 as opposed to 10^12 bytes) across several memory towers available as one unified address space with the local memory, bandwidth-intensive workloads can be accelerated without needing the compute to be throttled.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/kove_tower.png)

*Source: Viking Enterprise Solutions. Multiple memory towers can be combined in the same network fabric, with the address size being the limiting factor rather than physical space.*

At a high-level, the memory tower works by extending the main memory available to a host machine via network-attached DRAM, rather than adding more channels for DIMMs onto the host baseboard or connecting another board via PCIe. Kove supports [InfiniBand for the data plane](https://www.vikingenterprisesolutions.com/kovesdm-memory-tower/) (with RoCE support in the works) and Ethernet for the control plane, allowing for reasonably easy to manage addtional infrastructure in any standard ethernet-managed datacentre with a dedicated and isolated high-performance fabric for the data.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/kove_specs.png)

*Source: Kove.*

As for software, the [management and networking stack](https://kove.com/products/kovesdm-software/) works together to use a host server's local memory as a form of cache (think of it as L4/5), and keeps recently accessed and likely soon to be accessed within the host chassis. Remote memory then is able to serve as a nearly-identical access latency extension of this local cache, as the microseconds of time to RDMA data from the tower to host are likely amortized away by both the large bandwidth available on the network and the access prediction capabilities of the software.

---

# One-pagers:

## Bandwidth and latency

## Liquid cooling plates

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)