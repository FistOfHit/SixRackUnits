[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# April 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/title.jpeg)

*Will we ever move away from cables? What could high-bandwidth, low-error, and secure wireless communications looks like in the future?*

[**This month's updates:**](#this-months-updates)
  - [**Lightmatter's 3D photonics - computing with light**](#lightmatters-3d-photonics---computing-with-light)
  - [**Tenstorrent announces the BlackHole AI accelerator**](#tenstorrent-announces-the-blackhole-ai-accelerator)
  - [**IBM's z17 mainframe**](#ibms-z17-mainframe)
  - [**Ironwood: Google's seventh gen. TPU**](#ironwood-googles-seventh-gen-tpu)
  - [**China's answer to the NVL72 - Huawei's CloudMatrix 384**](#chinas-answer-to-the-nvl72---huaweis-cloudmatrix-384)
  - [**Other notable headlines**](#other-notable-headlines)

[**Vendor spotlight:**](#vendor-spotlight)
  - [**Kove**](#kove)

[**One-pagers:**](#one-pagers)
  - [**Bandwidth and latency**](#bandwidth-and-latency)
  - [**Liquid cooling plates**](#liquid-cooling-plates)

For a space to share sources and news/updates, join on <a href="https://t.me/aihpc_infra_fans">Telegram</a>, and check out my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a> for posts on similar topics!

---

# This month's updates:

## Lightmatter's 3D photonics - computing with light

## Tenstorrent announces the BlackHole AI accelerator

*American RISC chip/server design startup Tenstorrent seeks to take space in both the enterprise and retail AI accelerator markets with its low-power and easy to use PCIe card lineup, as well as servers designed around density and scaling. Their latest card, the BlackHole, seeks to offer a competitive price/performance ratio with a scale-up potential that appears to be significantly greater than what other PCIe devices from competitors such as Google and AWS can offer.*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/tenstorrent_blackhole.png)

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/tenstorrent_galaxy.png)

## IBM's z17 mainframe

*IBM mainframes are known for their near perfect uptime and low-latency for critical operations such as transaction processing, airline fleet management, and fraud detection to name a few. As more and more such workloads begin to use computationally expensive AI models, IBM's mainframes need to adapt to not just be better at what they already do, but also be better at the workloads of the near-future.*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/ibm_z17.png)

## Ironwood: Google's seventh gen. TPU

*In 2Q24 Google introduced the "Trillium" TPUv6 (Tensor processing unit), a continuation of their remarkably power-efficient series of custom AI accelerators available on GCP (Google cloud platform). Now, the series continues but with an unexpected progression: Inference and training are no-longer being assigned to two different versions in the same generation. The "Ironwood" TPUv7 appears to take on both workloads but the marketing around it confuses many.*

Google's latest in their custom silicon for AI workloads, the "Ironwood" TPUv7 has just been announced. It's unclear yet what stage of production it's at, or when it will be generally available for public GCP users, but some specs are available now. Of all the information provided, the most controversial statement made was a misguided (or even dishonest) comparison between a TPU "pod" and the worlds most computationally capable supercomputer, El Capitan.

The "Top500" organisation maintains a list of the worlds most powerful supercomputers ranked by their performance in a linear algebra benchmark. El capitan, placing first as of 4Q24, combines over 43,000 AMD MI300A APUs (CPU + GPU on the same package) to achieve a real performance of 1.74 exaFLOPs at FP64, with a theoretical peak at 2.74. TPUv7 pods on the other hand use their 2 or 3-dimensional torus network topology to combine 9,216 chips (not devices) into a single computational domain. 


![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/tpuv7.png)

## China's answer to the NVL72 - Huawei's CloudMatrix 384

*Nvidia's NVL72 was not the first but was certainly the most popular rack-scale, self-contained infrastructure solution built around AI accelerators. Densely packing this volume of high-powered chips into a single rack and interconnecting them with the NVLink scale-up network led to a product that could be easily integrated and used by hyperscalers and large businesses. But the NVL72 has its flaws, and Huawei is stepping up to take on Nvidia in this space too.*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/cloudmatrix384_picture.jpeg)

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/cloudmatrix384_diagram.png)

## Other notable headlines

* [SK-Hynix possibly mass producing both HBM4 and HBM4E this year](https://www.tweaktown.com/news/104464/sk-hynix-confirms-both-hbm4-and-hbm4e-memory-are-coming-this-year-for-next-gen-ai-gpus/index.html)
* [Chinese firms place up to $16 billion of orders for Nvidia's CHIPS act-dodging AI GPUs](https://www.reuters.com/technology/chinese-firms-place-16-billion-order-new-nvidia-chips-information-reports-2025-04-02/)
* [Samsung reportedly begins developing its 1nm "dream" process, ready for mass production in 2029](https://www.trendforce.com/news/2025/04/10/news-samsung-reportedly-begins-1nm-process-development-targets-2029-mass-production/)
* [Nubis communications and Amphenol to develop signal re-drivers to enable 200G/lane SERDES across multiple meters of copper, enabling multi-rack scale-up networks without optics](https://www.businesswire.com/news/home/20250326861856/en/CORRECTING-and-REPLACING-Nubis-Extends-Linear-Paradigm-from-Optics-to-Copper-with-Breakthrough-Nitro-Linear-Redriver-Solution-Enabling-4-Meter-Reach-for-200Gbps-per-Lane-Copper-Cables-in-AI-Scale-Up-Networks)
* [UALink (Ultra Accelerator Link) consortium announces their 1.0 specification, at 200G per lane. Aims to provide an open standard against Nvidia's NVLink](https://ualinkconsortium.org/)
* [Cadence reveals its HBM4 IP promising up to 12.8 Gbps per lane - 3.2TB/s over a 2048-wide bus for a single stack](https://www.ctol.digital/news/cadence-launches-128gbps-hbm4-ip-subsystem-for-ai-hpc/)
---

# Vendor spotlight:

## Kove

*Host memory capacity is and has always been the be-all and end-all of large, high-performance workloads, as triggering an OOM error usually causes not just the application and its progress/state to crash, but the entire host. [Kove](https://kove.com/) are a firm working to change this with a solution for remote, software-defined memory (SDM) that approaches the performance of local memory.*

Founded in 2003, American firm Kove has quietly been supplying remote memory solutions to customers who found their workloads constrained not by compute, but by memory capacity. Kove's memory tower system presents as a [rack](https://kove.com/products/kovesdm-memory-tower/) of DRAM enclosures containing some management compute and [high-performance NICs](https://arstechnica.com/sponsored/kove-tackles-the-last-software-defined-technology-memory/), and their [software stack](https://kove.com/products/kovesdm-software/) manages the remote memory and transfers to expose a memory pool that can be defined (configured or managed) entirely by software. With a maximum capacity of up to 256TiB (tebibyte, or 2^40 as opposed to 10^12 bytes) across several memory towers available as one unified address space with the local memory, bandwidth-intensive workloads can be accelerated without needing the compute to be throttled.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/kove_towers.png)

*Source: Viking Enterprise Solutions. Multiple memory towers can be combined in the same network fabric, with the address size being the limiting factor rather than physical space.*

At a high-level, the memory tower works by extending the main memory available to a host machine via network-attached DRAM, rather than adding more channels for DIMMs onto the host baseboard or connecting another board via PCIe. Kove supports [InfiniBand for the data plane](https://www.vikingenterprisesolutions.com/kovesdm-memory-tower/) (with RoCE support in the works) and Ethernet for the control plane, allowing for reasonably easy to manage additional infrastructure in any standard ethernet-managed datacentre with a dedicated and isolated high-performance fabric for the data.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/kove_specs.png)

*Source: Kove.*

As for software, the [management and networking stack](https://kove.com/products/kovesdm-software/) works together to use a host server's local memory as a form of cache (think of it as L4/5), and keeps recently accessed and likely soon to be accessed within the host chassis. Remote memory then is able to serve as a nearly-identical access latency extension of this local cache, as the microseconds of time to RDMA data from the tower to host are likely amortized away by both the large bandwidth available on the network and the access prediction capabilities of the software.

---

# One-pagers:

## Bandwidth and latency

*Bandwidth, being the amount of data transferred within a unit time and latency, being the time taken to complete a transfer of a unit size, these two key measurements in any data transfer are often misunderstood and misrepresented. Even worse, some will simple invert bandwidth and call it latency not realising their lack of consideration for overheads, measurement conditions, and variance, and the damage they do to the science.*

Measuring the performance of transferring data via a connection is usually done with two measurements: bandwidth and latency. 

Bandwidth measures the maximum volume of data that can be transferred through a connection in a given unit of time, and is measured as a rate such as Mbps (megabits per second). It's important to note that this is the maximum theoretical rate, not the actual or "realised" rate of data transfer across a connection. Bandwidth is often abstracted (applied to) or aggregated (accumulated) across a subset or an entirety of a network to give some indication of the potential rate that can be achieved for a workload using it. 

Latency on the other hand measures the time taken for a minimum unit volume of data to be transferred from a source to a destination, and is measured in units of time such as milliseconds. Some factors that influence latency like distance between endpoints or the speed/path of light in a material are physical and unavoidable, whilst others like the time to encode and decode signals are dependant on the hardware and protocols used for transmission. 

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/bandwidth_latency.png)

A common error made when measuring network performance is assuming that bandwidth is the inverse of latency, i.e. that a bandwidth of 100 Mbps implies a latency of 1/100 seconds. This assumption is ignores a few issues:
- Latency is only measured for a minimal sized transfer, one that should never be large enough to saturate a link for measuring bandwidth
- Bandwidth does not include the overheads involved with each minimal transfer, as these are amortized away when sending data in volume
- As the rate of transfer over w channel increases, so does contention and hence resource utilisation, which causes an increase in latency i.e. the relationship is non-linear

## Liquid cooling plates

*The height of air-cooled AI servers is influenced significantly by the size of the fans and the height of the heatsinks required to keep high-powered accelerator hardware cool. Compression attached cooling plates replace tall towers of metal fins in thinner-profile servers where getting enough airflow for cooling kilowatt+ devices either costs double-digit percentages of the servers total power draw, or is just physically impossible.*



![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/coolit_plate.png)

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)